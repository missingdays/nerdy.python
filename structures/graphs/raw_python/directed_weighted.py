'''
    type: structure
    theme: graphs
    sub-theme: implementation
    name: directed weighted graph
    author of code: Evgeny @missingdays Bovykin

'''

#Weighted directed graph

a, b, c, d, e, f, g, h = range(8)

N = [
    {b:2, c:1, d:3, e:9, f:4}, # a
    {c:4, e:3}, # b
    {d:8}, # c
    {e:7}, # d
    {f:5}, # e
    {c:2, g:2, h:2}, # f
    {f:1, h:6}, # g
    {f:9, g:8} # h
]
#Chech wheter b is linked to a
print(b in N[a])

#Get all nodes linked to f node
for node in N[f].keys():
    print(node)

#Get weight of a-b edge
print(N[a][b])
