def fibonacci(n):
    a,b = 0, 1 #First two numbers

    for i in range(2, n+1):
        a,b = b, a + b

    return a

for i in range(1, 10):
    print(fibonacci(i))
