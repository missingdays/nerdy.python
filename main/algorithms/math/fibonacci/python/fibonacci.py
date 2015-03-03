def fibonacci(n):
    
    if n == 1:
        return 0

    a,b = 0, 1 #First two numbers

    for i in range(2, n):
        a,b = b, a + b

    return b

for i in range(1, 10):
    print(fibonacci(i))
