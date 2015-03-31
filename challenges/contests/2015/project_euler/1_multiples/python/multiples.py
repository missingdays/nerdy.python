n = int(input())

def sum_list(a, d, N):

    s =  (2 * a + d * (N - 1)) * N / 2

    return s

for i in range(n):

    a = int(input())

    b,c,d = 0, 0, 0

    if a % 3 == 0:
        b = a // 3 - 1
    else:
        b = a // 3

    if a % 5 == 0:
        c = a // 5 - 1
    else:
        c = a // 5

    if a % 15 == 0:
        d = a // 15 - 1
    else:
        d = a // 15

    s = sum_list(3, 3, b) + sum_list(5, 5, c) - sum_list(15, 15, d)

    print(int(s))
