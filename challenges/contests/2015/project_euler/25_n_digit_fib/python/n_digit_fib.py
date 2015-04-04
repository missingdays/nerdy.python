def getDigits(number):
    return len(str(number))

digits = dict()
digits[0] = 0
def fib(n):
    digit = 1
    a, b = 0, 1
    c = 2
    while digit < n:
        a, b = b, a+b
        c = c + 1
        if getDigits(b) > digit:
            digit = digit + 1
            digits[digit-1] = c-1
fib(5000)
for i in range(int(input())):
    print(digits[int(input())-1])
