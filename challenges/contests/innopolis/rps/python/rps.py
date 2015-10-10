inputFile = open('rps.in', 'r')
outputFile = open('rps.out', 'w')

player1 = inputFile.readline().split()
player2 = inputFile.readline().split()

player1 = list(map(int, player1))
player2 = list(map(int, player2))
count = 0

count += min(player1[0], player2[1])
count += min(player1[1], player2[2])

count += min(player1[2], player2[0])


outputFile.write(str(count))
