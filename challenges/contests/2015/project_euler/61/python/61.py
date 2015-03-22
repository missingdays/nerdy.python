'''
    type: challenge solution
    theme: contest
    sub-theme: project euler
    name: 61
    author of code: Evgeny @missingdays Bovykin

'''
#Unstable!

#Triangle n * (n + 1) / 2
#Square n * n
#Pentagon n * (3 * n - 1) / 2
#Hexagon n * (2 * n - 1)
#Heptagon n * (5 * n - 3) / 2
#Octagon n * (3 * n - 2)

def getLast(n):

    return n % 100

def getFirst(n):

    return n // 100

types = []

types = input().split()

types = list(map(int, sizes))
