def prime_factors(n):
    i = 2
    factors = []

    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        factors.append(n)

    return factors    
