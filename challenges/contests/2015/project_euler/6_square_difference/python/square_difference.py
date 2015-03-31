def sum_nums(a):
    s = 0
    for i in range(a+1):
        s = s + i

    return s * s

def sum_sq(a):
    s = 0
    for i in range(a+1):
        s = s + i * i

    return s

for i in range(int(input())):
    a = int(input())
    print(sum_nums(a) - sum_sq(a))
    
