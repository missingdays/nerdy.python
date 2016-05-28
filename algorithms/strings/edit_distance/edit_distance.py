'''
    type: algorithm
    theme: string
    sub-theme: dynamic programming
    name: edit distance
    author of code: Evgeny @missingdays Bovykin

'''

#Get first string
s1 = input()

#Get second string
s2 = input()

#Array of distances
#row for s1
#columns for s2
distance = []

#Init array
for i in range(len(s1) + 1):

    column = [None] * (len(s2) + 1)

    distance.append(column)

#Init values
#to edit None to string it requires
#len(string) operations
for i in range(len(s1) + 1):

    distance[i][0] = i

for i in range(len(s2) + 1):

    distance[0][i] = i

#For every row
for i in range(1, len(s1) + 1):

    #And every column
    for k in range(1, len(s2) + 1):

        #If characters in this string are the same
        #we can either add one character to s1 (1 op)
        #or add one character to s2 (1 op)
        #or leave those charates to be (0 op)
        if s1[i-1] == s2[k-1]:

            distance[i][k] = min(
                distance[i-1][k] + 1,
                distance[i][k-1] + 1,
                distance[i-1][k-1]
            )
        #If characters in this string are not the same
        #we can either add one character to s1 (1 op)
        #or add one character to s2 (1 op)
        #or change one character to another (1 op)
        else :

            distance[i][k] = min(
                distance[i-1][k] + 1,
                distance[i][k-1] + 1,
                distance[i-1][k-1] + 1
            )

#Print final distance
print(distance[len(s1)][len(s2)])
