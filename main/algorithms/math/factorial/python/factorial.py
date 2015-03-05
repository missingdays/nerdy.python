def factorial(n):
    
    if n == 1 or n == 0:
        return 1

    a = 1

    for i in range(1, n+1):
        a = a * i

    return a

for i in range(1, 10):
    print("Factorial of ", i, "equals", factorial(i))
