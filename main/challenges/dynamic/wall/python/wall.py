import math

n = int(input())

array = [None] * n

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def dummyCalcPrime(a):
    count = 0
    i = 2
    for i in range(2, a+1):
        if is_prime(i):
            count = count + 1
    return count

for i in range(n):

    size = int(input())

    count = 1

    maximum = size // 4

    for k in range(1, maximum + 1):
        count = count + (size - k * 4) + 1
    print("c", count)
    array[i] = dummyCalcPrime(count)


for i in range(n):
    print(array[i])
