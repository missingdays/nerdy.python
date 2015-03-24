'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: chocolate feast
    author of code: Evgeny @missingdays Bovykin

'''


T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    N = int(N)
    C = int(C)
    M = int(M)

    answer = N // C
    b = N // C
    while b // M > 0:
        can_buy = b // M
        answer += can_buy
        b = b - can_buy * M + b // M
    print(int(answer))
