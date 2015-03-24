'''
    type: challenge solution
    theme: basic
    sub-theme: combinatorics
    name: handshakes
    author of code: Evgeny @missingdays Bovykin

'''


#For every test case
for i in range(int(input())):

    #Get number of people in the room
    n = int(input())

    #Calculate number of handshakes as
    #n * (n-1) / 2
    print(int(n * (n-1) / 2))
