
def is_palindrome(s, i):
    f = 0
    l = len(s) - 1

    while f < len(s)//2:
        if f == i:
            f += 1
        if s[f] != s[l]:
            return False
        l += 1
        f += 1
    return True

def get_index(s, n):
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            if is_palindrome(s, i):
                return i
            else:
                return n-i-1
    return -1

for i in range(int(input())):
    s = input()
    n = len(s)

    index = get_index(s, n)

    print(index)
