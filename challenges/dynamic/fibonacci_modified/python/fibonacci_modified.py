'''
    type: challenge solution
    theme: basic
    sub-theme: dynamic programming
    name: fibonacci modified
    author of code: Evgeny @missingdays Bovykin

'''

#Get input numbers
numbers = raw_input().split()

#Map them to ints
numbers = list(map(int, numbers))

#Get first number of sequence
first = numbers[0]

#Get second number of sequence
second = numbers[1]

#Calculte third number
third = first + second * second

#Get the nth index
nth = numbers[2]

#For every number in sequence to nth
for i in range(2, nth-1):

    #Replace first two numbers
    first, second= second, third

    #Calculate third
    third = first + second * second

#Print the answer!
print(third)
