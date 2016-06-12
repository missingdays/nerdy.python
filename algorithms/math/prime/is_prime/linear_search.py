
# Checks whether number is prime using simple linear search
def is_prime(n):

    # We need to check only first sqrt(n) numbers
    # Prove:
    #     Assume n divides some a > n/2. Than n divides n/a, that we will call b.
    #     Now lets assume that b is also > n/2.
    #     a > n/2
    #     b > n/2
    #     a*b > n
    #     So here we get contradiction. We know that a*b = n, but assuming that b > n/2 leads to a*b > n. So b can't be bigger that n/2, so 
    #     if n has divider bigger than n/2, it also has divider less than n/2.
    upper_bound = int(n**0.5)+ 1

    for divider in range(2, upper_bound):
        if n % divider == 0:
            return False
    
    return True
