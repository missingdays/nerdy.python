def checkPali(s):
    pali = True
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            pali = False

    return pali


for i in range(int(input())):
    index = -1
    s = input()

    for k in range(len(s)):
        if s[k] != s[len(s)-1-k]:
            if checkPali(s[:k] + s[k+1:]):
                index = k

    print(index)
