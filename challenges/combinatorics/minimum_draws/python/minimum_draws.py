'''
    type: challenge solution
    theme: basic
    sub-theme: combinatorics
    name: minimum draws
    author of code: Evgeny @missingdays Bovykin

'''


#Get number of test cases
n = int(input())

#For every test case
for i in range(n):

    #He needs to pull socks/2 (or number of pairs)
    #plus one to get at least one pair of one-color socks
    print(int(input()) + 1)
