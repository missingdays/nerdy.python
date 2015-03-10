#Returns every prime number up to the given one

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

print primes_sieve(200)
