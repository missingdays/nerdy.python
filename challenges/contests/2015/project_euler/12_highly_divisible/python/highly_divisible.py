import math
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor


n = int(input())

for i in range(n):

    a = []
    k = int(input())
    b = 1
    c = 2
    while len(a) <= k:
        b = b + c
        c = c + 1
        a = list(divisorGenerator(b))
        print(b, len(a))
    print(b)
