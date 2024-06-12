package main

import "fmt"
import "math/rand"
import "sync"
import "time"
import "unsafe"

// Struct to save an account
type Account struct {
    balance int
    mutex sync.Mutex // Status of whether the balance can be accesed or not
	history []string // A history of transactions on the account
}

// List of accounts
var accounts []*Account

// WaitGroup to wait for all transactions to finish
// It is like the channel because it allows us to block the code
var wg sync.WaitGroup

// Method to make a deposit
func (a *Account) Deposit(amount int) {

	// All inputs must be an amount of money, without sign
	if amount < 0 {
		amount = amount * -1
	}

	// Enter the critical zone by locking mutex
	a.mutex.Lock()

	/*
	"Defer" the unlock mutex operation. This is like a "finally" clause in Python
	We "schedule" the statement to be run at the end of the function's execution
	This way we make sure there are no deadlocks :)
	*/
	defer a.mutex.Unlock()

	// We add the amount to the account's balance
	a.balance += amount

	// Write the deposit in the history
	msg := fmt.Sprintf("Deposited $%d", amount)
	a.history = append(a.history, msg)
	// fmt.Println(msg) // Print to terminal
}

// Method to make a withdrawal from an account pointer
func (a *Account) Withdraw(amount int) bool {
	// All inputs must be an amount of money, without sign
	if amount < 0 {
		amount = amount * -1
	}

	// Enter the critical zone by locking mutex
    a.mutex.Lock()

	// Make sure we unlock the mutex at the end of the function
    defer a.mutex.Unlock()

	// Make the withdrawal only if the account has the specified amount
    if a.balance >= amount {
		// We subtract the amount from the account's balance
        a.balance -= amount

		// Write the withdraw in the history
		msg := fmt.Sprintf("Withdrew $%d", amount)
		a.history = append(a.history, msg)
		// fmt.Println(msg) // Print to terminal

        return true
    }

	// Else print error status in history
	a.history = append(a.history, "Withdraw failed: Insufficient funds")

    return false
}

// Transfer method
func (from *Account) TransferTo(to *Account, amount int) bool {
	/*
	When we perform transfers with concurrent systems we have to make sure that
	there are no deadlocks. One of the cases in which this can happen is when
	we make a transaction from A to B, and from B to A, at the same time. If both
	senders get locked, they will end up in an infinite loop trying to access the
	recepients account, each other.
	
	So, we must have a rule so that whenever a unique pair of
	accounts is going to make a transfer, we always prioritize transactions from one
	first and then the other. So, for example, always performing any transaction with
	A as a sender first over any transaction with B as a sender.

	To do this we can make use of the memory address of every account. We compare both and
	whatever hexadecimal value (memory address) is lower, is the account that we will always
	start operations with by locking it first.
	*/

	// All inputs must be an amount of money, without sign
	if amount < 0 {
		amount = amount * -1
	}

	// Can't transfer from and to the same account
	if from == to {
		// fmt.Println("Transfer failed: Same account")
		return false
	}

	// Lock the account with the lower memory address value first
	if uintptr(unsafe.Pointer(from)) < uintptr(unsafe.Pointer(to)) {
		from.mutex.Lock()
		to.mutex.Lock()
	} else {
		to.mutex.Lock()
		from.mutex.Lock()
	}

	// Schedule the mutex unlock at the end of the function
    defer from.mutex.Unlock()
    defer to.mutex.Unlock()

	// Perform transaction only if the sender has the specified amount
    if from.balance >= amount {
		// Make the transaction
        from.balance -= amount
        to.balance += amount

		// Write the transaction in both accounts history
		from.history = append(from.history, fmt.Sprintf("Transferred $%d to %p", amount, to))
		to.history = append(to.history, fmt.Sprintf("Received $%d from %p", amount, from))

		// Print to terminal
		// fmt.Printf("Transferred $%d from account %p to account %p\n", amount, from, to)

        return true
    }

	// Else print error status in history
	from.history = append(from.history, "Transfer failed: Insufficient funds")

    return false
}

// Function to perform some transactions randomly
func PerformTransactions() {

	// Remove from WaitGroup when we exit the function
	defer wg.Done()

	// Make 10 random actions
    for i := 0; i < 10; i++ {
		// Generate a random action between deposit, withdraw and transfer
        action := rand.Intn(3)

		// Select two random accounts from the account array
        account1 := accounts[rand.Intn(len(accounts))]
        account2 := accounts[rand.Intn(len(accounts))]

        // Generate a random amount for action between 1 and 1000
		amount := rand.Intn(1000) + 1

		// Execute action
        switch action {
			case 0:
				account1.Deposit(amount)
			case 1:
				account1.Withdraw(amount)
			case 2:
				account1.TransferTo(account2, amount)
        }

		// Small delay to make a bit slower and wait for other goroutines
        time.Sleep(time.Millisecond * 100)
    }
}

func main() {

	// Generate a random seed with current time
	rand.Seed(time.Now().UnixNano())

    // Initialize 10 accounts with a random balance > 1000 and < 3000
	for i := 0; i < 10; i++ {
		accounts = append(accounts, &Account{balance: rand.Intn(2000) + 1000})
	}

    // Call the random transactions function 5 times (for a total of 25 actions)
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go PerformTransactions()
	}

	// Wait for the transactions to finish
	wg.Wait()

	// Print the final balances
	for i, account := range accounts {
		fmt.Println("\n\n")
		fmt.Printf("Account %d (%p) balance: $%d\n", i+1, account,account.balance)
		fmt.Println("Account history:")
		for _, msg := range account.history {
			fmt.Println("-", msg)
		}
	}

	fmt.Println("\n\n")
}
