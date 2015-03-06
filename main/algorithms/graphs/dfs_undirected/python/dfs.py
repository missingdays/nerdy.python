a, b, c, d, e, f, g, h = range(8)

#Unweighted undirected graph
G = [
    [b, c, d, e, f], # a
    [a, c, e], # b
    [a, b, d], # c
    [a, c, e], # d
    [a, b, d, f], # e
    [a, c, g, e, h], # f
    [f, h], # g
    [f, g] # h
]

visited = [False] * len(G)


#Goes through every node in one connected component
def Explore(G, v):

    #Mark node as visited
    visited[v] = True

    #For every node
    for i in range(len(G[v])):

        #If that node is not visited
        if not visited[G[v][i]]:
            #Explore it
            Explore(G, G[v][i])

#Goes through every node in whole graph
def dfs(G):

    #Init
    for i in range(len(G)):
        visited[i] = False

    #For every node in graph
    for i in range(len(G)):

        #If that node is not visited yet
        if not visited[i]:
            #Explore it
            Explore(G, i)

dfs(G)
