n = int(input())

for i in range(n):
    s = list(input())
    count = 0

    for c in range(len(s)-1):
        if(s[c] == s[c+1]):
            count = count + 1

    print(count)
