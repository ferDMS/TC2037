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

        # Current state
        self.state = None
        # Last word(s)' states traversed
        self.steps = None
        # Last word(s)' parsed elements
        self.parsed = None
        # Criteria on which to parse at a given state or not
        self.parsing_criteria = None

    def execute(self, word, visualize=True, parse=True):
        # Set current state at initial state
        self.state = self.q

        # Check that the initial state is defined and in the list of states
        if not self.state or self.state not in self.Q:
            raise Exception("Initial state is not valid")

        # Display word to execute
        print(f"\nExecuting word: \"{word}\"")
        # Display initial state
        steps = [self.state]
        if visualize: print(f"[{self.state}]")
        # Initialize empty subword and an empty list of parsed subwords
        if parse:
            subword = ""
            parsed = []

        # Run word through automata
        for c in word:
            # Add character to subword
            subword += c
            # Perform step in dfa
            self.state = self.d[self.state][c]
            # Parse element based on previous state, current state, transition and current subword
            # If true, parse subword now and refresh it. Else, keep adding to it.
            if parse:
                save, keep = self.parsing_criteria(steps[-1], self.state, c, subword)
                if save: parsed.append((subword, steps[-1]))
                subword = subword if keep else c
            # Set current state and previous state, adding to steps
            steps.append(self.state)
            # Display source state and transition
            if visualize: print(f"'{c}' - [{self.state}]")
        
        # Add last remaining subword to parsed subwords if not empty
        if parse: 
            if len(subword): parsed.append((subword, self.state))
            self.parsed = parsed
        # Record steps of word
        self.steps = steps

        # Return whether the word is accepted or not based on final state
        return self.state in self.F
    

    def execute_list(self, words, visualize=True, parse=True):
        n = len(words)
        accepted = [0] * n
        # If visualize, save steps for all words in list
        steps = []
        # If parse, parse every words in list
        parsed = []
        # Execute for every word in the list
        for i in range(n):
            accepted[i] = self.execute(words[i], visualize=visualize, parse=parse)
            status = "accepted" if accepted[i] else "not accepted"
            print(f"The word is {status} by the language")
            steps.append(self.steps)
            if parse: 
                parsed.append(self.parsed)
                print(parsed[-1])
        self.steps = steps
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
    dfa.Q = {"s", "sign", "start_(", "start_await_comment", "single_dot", "int", "var", "float", "e", "e_sign", "float_e", "comment", "var_await_op", "await_op", "+", "-", "*", "^", "/", "=", "(", ")", "invalid", "success"}

    # Declare initial state
    dfa.q = "s"

    # Declare acceptance states
    dfa.F = {"s", "int", "var", "float", "float_e", "var_await_op", "await_op", "comment", "success"}

    # Declare parsing criteria
    def parsing_criteria(prev, curr, c, subword):
        # States that always save and reset a subword
        greedy_states = {"int", "var", "float", "comment"}
        parsing_states = greedy_states | {"float_e", "+", "-", "*", "^", "/", "=", "(", ")"}
        # ending_states = {"var_await_op", "await_op", "success"}

        # If the previous state is a state to be parsed
        if prev in parsing_states: 
            # If the state just repeated
            if curr == prev:
                # If it's a greedy state, let's keep add the char but not save the subword yet
                if curr in greedy_states: return (0, 1)
                # If it's not a greedy state but 
                # If it's not a greedy state, let's save the subword and reset it
                else: return (1, 0)
            # Else, the state is not repeated. Let's check if the prev state should be parsed or not
            elif prev in parsing_states: return (1, 0)
            # If the state shouldn't be parsed, don't save but keep subword
            else: return (0, 1)

        # Any other subwords can be kept but not saved
        return (0, 1)


    dfa.parsing_criteria = parsing_criteria

    # Set transitions of each state
    # We use a defaultdict because every character transition not explicitly defined will
    # transition to a default state. This is necessary because it is a DFA
    d = {state : defaultdict(lambda: "invalid") for state in dfa.Q}

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
    d["start_("][' '] = d["start_("]

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
        d[op][' '] = op
        d[op]['('] = "("
        d[op]['.'] = "single_dot"
        for c in _d: d[op][c] = "int"
        for c in ['-', '+']: d[op][c] = "sign"
        for c in _w_noDigits: d[op][c] = "var"
    
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

    # Transitions of the "invalid" state
    # All characters bring you back to the same state
    # d["invalid"] = defaultdict(lambda: "invalid")
    # ---------------------------------------------------------------------------------------

    # Assign transitions to dfa object
    dfa.d = d