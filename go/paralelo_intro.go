package main
import (
	"time"
	"fmt"
	"math/rand"
)

func pequenioDurmiente() {
	time.Sleep(5 * time.Second)
	fmt.Println("Soy un hilo")
}

func dormir(id int, c chan in) {
	time.Sleep(time.Duration(rand.Intn(4000)) * time.Millisecond)
	fmt.Println("He despertado. ID=", id)
	c <- id
}

func main() {

	// Canal, como un rio
	c := make(chan int)
	for i := 0, i < 5; i++ {
		go dormir(i, c)
	}

	timeout := time.After(5 * time.Second)
	for i := 0; i < 5; i++ {
		select {
		case gopherID := <-c:
			fmt.Println("Proceso: ", gopherID, " ha despertado")
		case <- timeout:
			fmt.Println("time out")
			return
		}
	}
	
	for i := 0, i < 10; i++ {
		pequenioDurmiente(i)
	}

	fmt.Println("*******************")

	for i := 0; i < 10; i++ {
		go pequenioDurmiente(i)
	}
}

