
a = int(input())

if a % 2 == 1:
    print(0)
else:
    a //= 2
    if a % 2 == 0:
        a -= 1

    print(a // 2)    

