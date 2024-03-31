from helper import DFA
from helper import setSolutionDFA


def lexerAritmetico(archivo):
    # Open file and parse content into list of expressions
    with open(archivo) as file:
        expressions = []
        line = file.readline()
        while line:
            expressions.append(line.strip())
            line = file.readline()
        
    # Visualize arithmetic expressions
    print("\nExpresiones arirtmeticas\n--------------------------")
    for exp in expressions: print(exp)
    print("--------------------------")

    # Initialize DFA and its properties
    dfa = DFA()
    setSolutionDFA(dfa)

    # Run DFA with expressions
    accepted = dfa.execute_list(expressions)
    print(dfa.parsed)
    


lexerAritmetico("expresiones.txt")
    