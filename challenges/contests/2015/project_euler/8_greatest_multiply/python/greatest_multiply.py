n = int(input())
def multi(number):
    mult = 1
    for digit in number:
        mult = mult * int(digit)

    return mult

for i in range(n):

    loop = int(input().split()[1])

    number = input()

    m = 0

    for i in range(len(number)-loop+1):
        a = multi(number[i:i+loop])
        print(number[i:i+loop])
        if a > m:
            m = a

    print(m)
