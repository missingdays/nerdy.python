'''
    type: challenge solution
    theme: basic
    sub-theme: combinatorics
    name: connecting towns
    author of code: Evgeny @missingdays Bovykin

'''


for i in range(int(input())):

    input()

    n = raw_input().split()

    n = list(map(int, n))

    answ = 1

    for k in range(len(n)):

        answ = (answ * n[k]) % 1234567

    print(answ)
