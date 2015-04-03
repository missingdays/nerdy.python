def calc(s):
    su = 0
    for c in s:
        su += ord(c) - ord('A') + 1
    return su
n = int(input())

names = []

for i in range(n):
    names.append(input())

names.sort()

scores = []

for i in range(n):
    scores.append(calc(names[i])*(i+1))

n = int(input())

for i in range(n):
    print(scores[names.index(input())])
