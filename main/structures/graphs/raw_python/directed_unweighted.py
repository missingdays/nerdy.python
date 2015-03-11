'''
    type: structure
    theme: graphs
    sub-theme: implementation
    name: directed unweighted graph
    author of code: Evgeny @missingdays Bovykin

'''


#Unweighted graph

a, b, c, d, e, f, g, h = range(8)

N = [
    [b, c, d, e, f], # a
    [c, e], # b
    [d], # c
    [e], # d
    [f], # e
    [c, g, h], # f
    [f, h], # g
    [f, g] # h
]
#Chech wheter b is linked to a
print(b in N[a])

#Get all nodes linked to f node
for i in range(len(N[f])):
    print(N[f][i])
