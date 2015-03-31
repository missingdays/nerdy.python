'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: find digits
    author of code: Evgeny @missingdays Bovykin

'''

#Get number of test cases
n = int(input())

#For each test case
for i in range(n):

    #Get number as string
    number = input()

    #Number as string
    number_int = int(number)

    #Counter of all digits that divide number
    count = 0

    #For every digit in number
    for digit in number:

        #Conver in to int
        a = int(digit)

        #We can't divide by zero
        if a != 0:

            #If a divides number
            if number_int % a == 0:

                #Increment counter
                count = count + 1

    #Print how much digits divide the number
    print(count)
