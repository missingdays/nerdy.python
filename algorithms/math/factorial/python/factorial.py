'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: factorial
    author of code: Evgeny @missingdays Bovykin

'''

def factorial(n):

    if n == 1 or n == 0:
        return 1

    a = 1

    for i in range(1, n+1):
        a = a * i

    return a

if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(20) == 2432902008176640000
    print("Factorial python done")