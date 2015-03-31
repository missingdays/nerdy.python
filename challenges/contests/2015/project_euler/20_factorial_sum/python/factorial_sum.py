from math import factorial

#Function to calculate sum of all digits in a number
def sum_digits(n):

    #Sum
    digit_sum = 0

    #For every digit in a number
    while n:

        #Add this digit to sum
        #and pop it from a number
        digit_sum, n = digit_sum + n % 10, n / 10

    #Return sum
    return digit_sum

#Get number of test cases
n = int(input())

#For every test case
for i in range(n):

    #Get number
    a = int(input())

    #Calculate factorial
    fac = factorial(a)

    #Print sum of all digits
    print(sum_digits(fac))
