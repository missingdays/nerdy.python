'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: alternating characters
    author of code: Evgeny @missingdays Bovykin

'''


#Number of test cases
n = int(input())

#For every test case
for i in range(n):

    #Set count to 0
    count = 0

    #Read string to be calculated
    string = input()

    #For every character in that string
    #to the middle of the string
    for c in range(int(len(string) / 2)):

        #Character from the left part of the string
        left = string[c]

        #Character from the right part of the string
        right = string[len(string) - 1 - c]

        #Calculate how many operations needs to be done
        #to turn one character to another
        count += abs(ord(right) - ord(left))

    #Print sum of all differences
    print(count)
