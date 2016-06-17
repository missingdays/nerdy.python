'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: Euclidian algorithm (greatest common division)
    author of code: Evgeny @missingdays Bovykin

'''

def gcd(a,b):
    """
    Finds greatest common divisor using Euclidean Algorithm
    """

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return max(a, b)
