s1 = input()
s2 = input()

distance = []

for i in range(len(s1) + 1):

    column = [None] * (len(s2) + 1)

    distance.append(column)


for i in range(len(s1) + 1):

    distance[i][0] = i

for i in range(len(s2) + 1):

    distance[0][i] = i

for i in range(1, len(s1) + 1):

    for k in range(1, len(s2) + 1):

        if s1[i-1] == s2[k-1]:

            distance[i][k] = min(
                distance[i-1][k] + 1,
                distance[i][k-1] + 1,
                distance[i-1][k-1]
            )

        else :

            distance[i][k] = min(
                distance[i-1][k] + 1,
                distance[i][k-1] + 1,
                distance[i-1][k-1] + 1
            )
print(distance[len(s1)][len(s2)])
