'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: fibonacci
    author of code: Evgeny @missingdays Bovykin

'''

def fibonacci(n):

    if n == 1:
        return 0

    a,b = 0, 1 #First two numbers

    for i in range(2, n):
        a,b = b, a + b

    return b

if __name__ == "__main__":
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8
    assert fibonacci(8) == 13
    assert fibonacci(9) == 21
    assert fibonacci(10) == 34

    print("Fibonacci python done")