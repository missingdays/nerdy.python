'''
    type: challenge solution
    theme: contest
    sub-theme: project euler
    name: 67 - max parh
    author of code: Evgeny @missingdays Bovykin

'''


def findMax(array):
    m = array[0]

    for i in range(1,len(array)):
        if array[i] > m:
            m = array[i]

    return m


for i in range(int(input())):

    size = int(input())

    field = []



    for k in range(size):

        row = raw_input().split()

        row = list(map(int, row))

        field.append(row)


    way = [None]*size

    for k in range(size):
        way[k] = [None] * size

    way[0][0] = field[0][0]

    for k in range(1, size):

        for l in range(k+1):

            if l != 0 and l != k:
                way[k][l] = max(field[k][l] + way[k-1][l-1], field[k][l] + way[k-1][l])


            elif l == 0:

                way[k][l] = field[k][l] + way[k-1][l]

            else:

                way[k][l] = field[k][l] + way[k-1][l-1]



    print(findMax(way[size-1]))
