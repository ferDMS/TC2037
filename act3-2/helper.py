from collections import defaultdict 


class DFA:
    def __init__(self):
        # States
        self.Q = None
        # Transitions
        self.d = None
        # Initial state
        self.q = None
        # Final state
        self.F = None

        # Invalid / Null / Unescapable State
        self.invalid = None
        # Last word(s)' states traversed
        self.log = None
        # Last word(s)' parsed subwords
        self.parsed = None
        # Criteria on which to parse at a given state or not
        self.parsing_criteria = None

    def execute(self, word, visualize=True, parse=True):
        # Set current state at initial state
        curr = self.q
        # Start count of number of transitions made
        n_steps = 0
        # Check that the initial state is defined and in the list of states
        if not curr or curr not in self.Q:
            raise Exception("Initial state is not valid")
        
        # Display word to execute
        print(f"\nExecuting word: \"{word}\"")
        # Initialize log of states with initial state
        log = [curr]

        # If debugging, display initial state
        # print(f"[{curr}]")

        # If parsing, initialize empty subword and an empty list of parsed subwords
        if parse:
            parsed = []
            # Define variable to save concatenation of transition characters (subword)
            subword = ""

        # Run word through automata
        for c in word:
            # Perform transition in dfa to check next state
            next_ = self.d[curr][c]

            # If the next state is the invalid state, then we raise an error
            if next_ == self.invalid:
                msg = (
                    "---------------------------------------\n"
                    f"Syntax error at index {n_steps}: '{word[n_steps]}'\n"
                    f"Last state recorded: [{curr}]\n"
                    f"{word}\n"
                    f"{"":>{n_steps}}^ Error\n"
                    "---------------------------------------"
                )
                print(msg)
                curr = next_
                break
            
            # If debugging, display transition and next state
            # if visualize: print(f"'{c}' - [{next_}]")

            # If parsing, parse character based on current and next state
            if parse:
                save, keep = self.parsing_criteria(curr, next_)
                if save:  
                    parsed.append((subword, curr))
                if keep: 
                    subword += c
                else: 
                    subword = c

            # Set current state as the next state for the following iteration
            curr = next_
            # Add state to log
            log.append(curr)
            # Increase steps done
            n_steps += 1
        
        # Define whether the word was accepted or not based on the final state
        accepted = curr in self.F

        # If visualizing
        if visualize:
            status = "accepted" if accepted else "not accepted"
            print(f"The word is {status} by the language")

        # If parsing
        if parse: 
            # Add last remaining subword depending on criteria
            save, keep = self.parsing_criteria(curr, None) # No next transition
            if save:  parsed.append((subword, curr))
            # Update list of parsed subwords
            self.parsed = parsed
            # If also visualizing
            if visualize:
                # Print the parsed subwords
                print(parsed)
        # Record log of word
        self.log = log
        print()

        # Return the acceptance status of the word
        return accepted
    

    def execute_list(self, words, visualize=True, parse=True):
        n = len(words)
        # List of acceptance status for all words in the list
        accepted = [0] * n
        # Log of logs, each for the states of all words in the list
        log = []
        # If parsing, parse every words in list
        if parse: parsed = []
        # Execute for every word in the list
        for i in range(n):
            # Execute word and add its states to log of logs
            accepted[i] = self.execute(words[i], visualize=visualize, parse=parse)
            log.append(self.log)
            # If parsing, add to list of parsed words
            if parse: 
                parsed.append(self.parsed)
        self.log = log
        if parse: self.parsed = parsed
        return accepted


# Whole number (WN):     (\d+)
# Variable (V):          ([a-zA-Z_]\w*)
# Decimal number (DN):   ((?:\d+\.\d*|\.\d+)(?:[eE][-+]?\d)?)
# Comment (C):           (\/\/.*$)

# Numbers with sign (N): ([-+]?(?:{DN}|{WN}))
# which also equals:     ([-+]?(?:(?:\d+\.\d*|\.\d+)(?:[eE][-+]?\d)?|(?:\d+)))


def setSolutionDFA(dfa):
    # The alphabet of the automata is every character available in Unicode

    # Declare all the states of the automata
    dfa.Q = {"s", "sign", "start_(", "start_await_comment", "single_dot", "int", "var", "float", "e", "e_sign", "float_e", "comment", "var_await_op", "await_op", "+", "-", "*", "^", "/", "=", "(", ")", "await_value", "invalid", "success"}

    # Declare initial state
    dfa.q = "s"

    # Declare acceptance states
    dfa.F = {"s", "int", "var", "float", "float_e", "var_await_op", "await_op", "await_value", "comment", "success"}

    # Declare parsing criteria
    def parsing_criteria(curr, next_):
        # States that should be parsed
        to_parse = {"int", "var", "float", "float_e", "+", "-", "*", "^", "/", "=", "(", ")", "comment"}

        # States that can or not be parsed but that always extend a subword
        # By extending is meant to keep the subword
        extends = {"float", "float_e", "e", "e_sign", "comment"}

        # If the next state extends the current state
        if next_ in extends:
            # Don't save yet and keep the word
            return 0, 1

        # If current state shouldn't be parsed
        if curr not in to_parse:
            # Don't save and don't keep the word
            return 0, 0

        # If current state should be parsed
        else:
            # If state doesn't change on transition
            if curr == next_:
                # Don't save yet and keep the word
                return 0, 1
            
            # If state changes on transition
            else:
                # Save and don't keep the word
                return 1, 0

    dfa.parsing_criteria = parsing_criteria

    # Declare invalid state
    dfa.invalid = "invalid"

    # Declare transitions of each state
    # We use a defaultdict because every character transition not explicitly defined will
    # transition to the invalid state. This is necessary because it is a DFA
    d = {state : defaultdict(lambda: dfa.invalid) for state in dfa.Q}

    # ---------------------------------------------------------------------------------------
    # Define ranges of common chracters
    _d = [str(i) for i in range(0,10)]
    _w_noDigits = [chr(i) for i in list(range(65, 91)) + list(range(97, 123)) + [95]]
    _w = _w_noDigits + [chr(i) for i in list(range(48, 58))]

    # Define common transitions to operator states ['+', '-', '*', '^', '/']
    _o = ['+', '-', '*', '^', '/']

    # Transitions of the "start" state
    d["s"][' '] = "s"
    for c in ['+', '-']: d["s"][c] = "sign"
    d["s"]['/'] = "start_await_comment"
    d["s"]['.'] = "single_dot"
    for c in _d: d["s"][c] = "int"
    for c in _w_noDigits: d["s"][c] = "var"
    d["s"]['\n'] = "success"
    d["s"]['('] = "start_("

    # Transitions of the "sign" state
    d["sign"]['.'] = "single_dot"
    for c in _d: d["sign"][c] = "int"
    
    # Transitions of the "start_(" state
    # Same as start state but the transition to self changes
    d["start_("] = d["s"]
    d["start_("][' '] = "start_("

    # Transitions of the "start_await_comment" state
    d["start_await_comment"]['/'] = "comment"
 
    # Transitions of the "single_dot" state
    for c in _d: d["single_dot"][c] = "float"

    # Transitions of the "int" state
    for c in _d: d["int"][c] = "int"
    d["int"]['.'] = "float"
    d["int"][' '] = "await_op"
    d["int"][')'] = ")"
    for c in _o: d["int"][c] = c
    d["int"]['\n'] = "success"

    # Transitions of the "var" state
    for c in _w: d["var"][c] = "var"
    d["var"][' '] = "var_await_op"
    d["var"][')'] = "var_)"
    for c in _o: d["var"][c] = c
    # Additional transition to perform assignment
    d["var"]['='] = "="
    d["var"]['\n'] = "success"

    # Transitions of the "float" state
    for c in _d: d["float"][c] = "float"
    for c in ['e', 'E']: d["float"][c] = "e"
    d["float"][' '] = "await_op"
    d["float"][')'] = ")"
    for c in _o: d["float"][c] = c
    d["float"]['\n'] = "success"

    # Transitions of the "e" state
    for c in _d: d["e"][c] = "float_e"
    for c in ['+', '-']: d["e"][c] = "e_sign"

    # Transitions of the "e_sign" state
    for c in _d: d["e_sign"][c] = "float_e"

    # Transitions of the "float_e" state
    d["float_e"][' '] = "await_op"
    d["float_e"][')'] = ")"
    for c in _o: d["float_e"][c] = c
    d["float_e"]['\n'] = "success"

    # Transitions of the "comment" state
    # All characters bring you back to the same state except new line
    d["comment"] = defaultdict(lambda: "comment")
    d["comment"]['\n'] = "success"

    # Transitions of the "await_op" state
    d["await_op"][' '] = "await_op"
    d["await_op"][')'] = ")"
    for c in _o: d["await_op"][c] = c
    d["await_op"]['\n'] = "success"

    # Transitions of the "var_await_op" state
    # Similar to "await_op"
    d["var_await_op"][' '] = "var_await_op"
    d["var_await_op"][')'] = "var_)"
    for c in _o: d["var_await_op"][c] = c
    d["var_await_op"]['\n'] = "success"
    # but with an additional valid transition to "="
    d["var_await_op"]['='] = "="

    # Transitions of the operator states ['+', '-', '*', '^', '/', '=', '(']
    for op in _o + ['=', '(']:
        d[op][' '] = "await_value"
        d[op]['('] = "("
        d[op]['.'] = "single_dot"
        for c in _d: d[op][c] = "int"
        for c in ['-', '+']: d[op][c] = "sign"
        for c in _w_noDigits: d[op][c] = "var"
    
    # Additionally, the "(" state can receive ')' immediatelly
    d["("][')'] = ")"

    # Transitions of the "await_value" state
    d["await_value"][' '] = "await_value"
    d["await_value"]['('] = "("
    d["await_value"]['.'] = "single_dot"
    for c in _d: d["await_value"][c] = "int"
    for c in ['-', '+']: d["await_value"][c] = "sign"
    for c in _w_noDigits: d["await_value"][c] = "var"
    
    # Transitions of the ")" state
    # Same as await_op but we stay in this state with ' '
    d[")"] = d["await_op"]
    d[")"][' '] = ")"

    # Transitions of the "var_)" state
    # Same as var_await_op but we stay in this state with ' '
    d["var_)"] = d["var_await_op"]
    d["var_)"][' '] = "var_)"

    # Add unique transition of "/" to be able to complete a comment
    d["/"]['/'] = "comment"

    # Transitions of the "success" state
    # All characters bring you back to the same state
    d["success"] = defaultdict(lambda: "success")
    d["success"][" "] = "success"

    # Transitions of the "invalid" state
    # All characters bring you back to the same state
    d["invalid"] = defaultdict(lambda: "invalid")
    d["invalid"][" "] = "invalid"
    # ---------------------------------------------------------------------------------------

    # Assign transitions to dfa object
    dfa.d = d