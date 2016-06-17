'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: fibonacci
    author of code: Evgeny @missingdays Bovykin

'''

def fibonacci(n):
    """
    Computing Fibonacci n-th number using simple dynamic approach
    Numbers are indexed from 1, so
    F(1) = 0
    F(2) = 1
    F(3) = 1
    F(4) = 2
    And so on
    """

    if n == 1:
        return 0

    a,b = 0, 1

    for i in range(2, n):
        a,b = b, a + b

    return b