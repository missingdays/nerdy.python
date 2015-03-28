def arraysum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]

    return sum
answ = []
for i in range(int(input())):

    n = list(map(int, input().split()))
    a = n[1]

    pl1 = list(map(int, input().split()))

    pl2 = list(map(int, input().split()))

    pl1.sort()

    pl2.sort()

    pl1 = pl1[:a]
    pl2 = pl2[len(pl2)- a:]

    if(arraysum(pl1) > arraysum(pl2)):

        answ.append("YES")

    else:
        answ.append("NO")

for i in range(len(answ)):
    print(answ[i])
