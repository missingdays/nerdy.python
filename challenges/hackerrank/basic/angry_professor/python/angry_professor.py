'''
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: angry professor
    author of code: Evgeny @missingdays Bovykin

'''
#Get number of testcases
n = int(input())

#For every test case
for i in range(n):

    #Get minimum number of students required
    min_studs = int(input().split()[1])

    #Counter of students that arrived in time
    count = 0

    #Get all students arrival time
    studs = list(map(int, input().split()))

    #For every student
    for stud in studs:

        #If that student arrived in time
        if stud <= 0:

            #Count him
            count = count + 1

    #If not enough students arrived in time
    if count < min_studs:

        #The class is cancelled
        print("YES")

    #Else
    else:

        #It's not
        print("NO")
