'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: halloween party
    author of code: Evgeny @missingdays Bovykin

'''


#Get number of test cases
n = int(input())

#For each test case
for i in range(n):

    #Get number of cuts
    k = int(input())

    #Maximum square can be achieved
    #if we multiply two numbers next to each other.
    #For example, if a + b = 7
    #the biggest multiply we can get is 3(a) * 4(b) = 12
    #Calculate the first number
    a = k // 2

    #Calculate the second number
    b = k - a

    #Print square that we get
    print(a * b)
