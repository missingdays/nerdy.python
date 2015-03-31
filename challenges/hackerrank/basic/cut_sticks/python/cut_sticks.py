'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: chocolate feast
    author of code: Evgeny @missingdays Bovykin

'''


#Get numbers of sticks(we dont need them in Python :P )
input()

#Get list of sticks
sticks = list(map(int, input().split()))

#While there are sticks left
while len(sticks) > 0:

    #Print how much sticks we are going to cut
    print(len(sticks))

    #Find the smallest stick
    #Assume the smallest stick is the first
    least = sticks[0]

    #Compare is with all other sticks
    for i in range(1, len(sticks)):

        #If that stick is smaller than our current smallest
        if sticks[i] < least:

            #Now smallest is this stick
            least = sticks[i]

    #While we didn't reach the end of the list
    i = 0
    while i < len(sticks):

        #Cut every stick
        sticks[i] = sticks[i] - least

        #Pop the stick that was fully cut
        if sticks[i] == 0:
            sticks.pop(i)

        #Or increment counter
        else:
            i = i + 1
