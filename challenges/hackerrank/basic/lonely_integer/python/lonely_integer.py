'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: lonely integer
    author of code: Evgeny @missingdays Bovykin

'''


#Function that finds lonely integer
def lonelyinteger(b):

    #Set answer to 0
    answer = 0

    #For every integer in b
    for i in range(len(b)):

        #If it's not in left and right parts of the array
        if not b[i] in b[0:i] and not b[i] in b[i+1:len(b)]:

            #That means this integer is lonely
            answer = b[i]

    #Return this integer
    return answer
# Tail starts here
if __name__ == '__main__':

    #Get number of integers
    a = int(input())

    #Get all those integers as string
    b = input().split(" ")

    #Convert them to integers
    b = [int(x) for x in b]

    #Print the lonely integer
    print(lonelyinteger(b))
