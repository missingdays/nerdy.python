'''
    type: challenge solution
    theme: contest
    sub-theme: russian code cup 2015
    name: b - homework
    author of code: Evgeny @missingdays Bovykin

'''
#Function to calc sum of all numbers
#in array
def arraysum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]

    return sum

#Where we will store our answers
#to output them after all calculations
answ = []

#For every testcase
for i in range(int(input())):

    #Get how many cards will be drawn
    n = list(map(int, input().split()))
    a = n[1]

    #Get first player's cards
    pl1 = list(map(int, input().split()))

    #Get second player's cards
    pl2 = list(map(int, input().split()))

    #Sort them both
    pl1.sort()

    pl2.sort()

    #Get minimum of first player's cards
    pl1 = pl1[:a]

    #And maximum of second player's cards
    pl2 = pl2[len(pl2)- a:]

    #If sum of minimum of first player's cards
    #is larger then sum of maximum of second player's cards
    if(arraysum(pl1) > arraysum(pl2)):

        #First player will win in any case
        answ.append("YES")

    #Else
    else:

        #He will not
        answ.append("NO")

#For every answer
for i in range(len(answ)):

    #Print that answer
    print(answ[i])
