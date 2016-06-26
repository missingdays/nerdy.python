
def gcd(a,b):
    """
    Finds greatest common divisor using Euclidean Algorithm
    """

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return max(a, b)

def lcm(a, b):
    """
    Finds least common multiply
    """
    return a * b / gcd(a, b)
def factorial(n):
    if n == 1 or n == 0:
        return 1

    a = 1

    for i in range(1, n+1):
        a = a * i

    return a

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

def fibonacci(n):
    """
    Computing Fibonacci n-th number using simple dynamic approach
    Numbers are indexed from 1, so
    F(1) = 0
    F(2) = 1
    F(3) = 1
    F(4) = 2
    And so on
    """

    if n == 1:
        return 0

    a,b = 0, 1

    for i in range(2, n):
        a,b = b, a + b

    return b

def fibonacci_mod(n, m):
    """
    Fast Fibonacci mod m computing
    """
    
    a11 = 1
    a12 = 1
    a21 = 1
    a22 = 0
    r11 = 1
    r12 = 0
    q11 = 0 
    q12 = 0
    q21 = 0 
    q22 = 0
    while n > 0:
        if (n&1) == 1:
            q11 = (r11 * a11 + r12 * a21) % m
            q12 = (r11 * a12 + r12 * a22) % m
            r11 = q11
            r12 = q12
        q11 = (a11 * a11 + a12 * a21) % m
        q12 = (a11 * a12 + a12 * a22) % m
        q21 = (a21 * a11 + a22 * a21) % m
        q22 = (a21 * a12 + a22 * a22) % m
        a11 = q11
        a12 = q12
        a21 = q21
        a22 = q22
 
        n >>= 1

    return r12

def pi_digits():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr

def calc(pol, x):
	result = pol[0]
	for i in range(1, len(pol)):
		result *= x
		result += pol[i]
	return result
	
