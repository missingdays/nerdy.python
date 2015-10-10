fl = list(map(int, input().split()))

k = fl[1]

colors = list(map(int, input().split()))

gift = []
a = 0
while a < len(colors):

    if not colors[a] in gift:
        gift.append(colors.pop(a))
    else:
        a = a + 1

while k > len(gift):

    gift.append(colors.pop())

for i in range(len(gift)):
    print(gift[i])
