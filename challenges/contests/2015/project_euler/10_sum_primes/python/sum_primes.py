def primes_sieve(limit):

    #Include number itself
    limitn = limit+1

    #Create new dictionary where we will store out numbers
    primes = dict()

    #Mark every number as prime
    for i in range(2, limitn): primes[i] = True

    #For every prime number
    for i in primes:

        #For every multiples of this prime number
        factors = range(i, limitn, i)

        #Except this prime number
        for f in factors[1:]:

            #Mark them as composite number
            primes[f] = False

    #Return all numbers that haven't been marked as composite
    return [i for i in primes if primes[i]==True]
array = primes_sieve(1000000)
sums = [None] * 1000000
sums[0] = 2
for i in range(1, len(array)):
    sums[i] = sums[i-1] + array[i]
for i in range(int(input())):
    r = len(array)-1
    l = 0
    i = r // 2
    n = int(input())
    while not(array[i] <= n and array[i+1] > n):
        if array[i] > n:
            r = i - 1
            i = (r + l) // 2
        elif array[i] < n:
            l = i + 1
            i = (r + l) // 2

    print(sums[i-1])
