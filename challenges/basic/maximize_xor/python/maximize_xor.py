'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: maximize xor
    author of code: Evgeny @missingdays Bovykin

'''

def maxXOR(x, y):

    #Set maximum to zero
    maximum = 0

    #For every number from x to y
    for i in range(x, y+1):

        #For every number from x to y
        for k in range(x, y+1):

            #Compare their XOR to temporary maximum
            #if it's bigger than temporary maximum
            if i ^ k > maximum:

                #Set maximum to its XOR
                maximum = i ^ k

    #Return final maximum
    return maximum
if __name__ == '__main__':

    #Get first number
    x = int(input())

    #Get second number
    y = int(input())

    #Print their maxXOR
    print(maxXOR(x, y))
