n = int(input())
way = [None] * (500)
for k in range(500):
    temp = [None] * (500)
    way[k] = temp

for k in range(len(way)):
    way[k][0] = 1
for k in range(len(way[0])):
    way[0][k] = 1

for k in range(1, len(way)):
    for j in range(1, len(way[0])):
        way[k][j] = (way[k][j-1] + way[k-1][j]) % 1000000007
for i in range(n):
    size = list(map(int, input().split()))


    print(way[size[0]][size[1]])
