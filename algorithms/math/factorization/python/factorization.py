
import collections

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

if __name__ == "__main__":
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

    assert compare([2, 3], prime_factors(6))
    assert compare([2, 2], prime_factors(4))
    assert compare([2, 2, 2], prime_factors(8))
    assert compare([2, 3, 5, 7], prime_factors(210))
    assert compare([2, 5, 7], prime_factors(70))
    assert compare([11, 13], prime_factors(143))
    assert compare([31, 31], prime_factors(961))
    assert compare([523], prime_factors(523))
    assert compare([523, 523, 523, 523], prime_factors(74818113841))

    print("Factorization python done")
