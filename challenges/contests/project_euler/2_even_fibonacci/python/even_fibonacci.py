
#Get number of test cases
n = int(input())

#Function to calculate sum of even numbers of Fibonacci
def fib_sum(n):

    #Sum to be returned
    s = 0

    #First two numbers of the sequence
    a, b = 0, 1

    #While we don't exceed n
    while b < n:

        #Calculate next number
        a, b = b, a + b

        #If number is even
        if a % 2 == 0:

            #Add it to sum
            s = s + a

    #Return sum
    return s

#For every test case
for i in range(n):

    #Get n
    n = int(input())

    #Print sum
    print(fib_sum(n))
