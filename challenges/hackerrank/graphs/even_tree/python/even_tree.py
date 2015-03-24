#Get number of edges
n = int(input().split()[1])

#Init forest with n + 1 edges
forest = [None] * (n + 1)

for i in range(len(forest)):
    forest[i] = []

#Array to check wether we visited vertex or not
visited = []

#Get forest from inputs
for i in range(n):

    #Get new edge as array of two integers
    edge = list(map(int, input().split()))

    #Add edges to both vertexes
    forest[edge[0] - 1].append(edge[1] - 1)
    forest[edge[1] - 1].append(edge[0] - 1)

#How much we cut so far
count = 0

#Main function that calculates components and counts
def getComponents(v, forest, count):

    #If we haven't visited this vertex yet
    if not v in visited:


        #Now we visited this vertex
        visited.append(v)

        #Vertex itself counts in components
        vertexesInComponent = 1

        #For every vertex that is linked to current vertex
        for i in range(len(forest[v])):

            #If we haven't visited this vertex yet
            if not forest[v][i] in visited:

                #Get how much childs that vertex has
                #and how much we can cut on that component
                vertexesInChildComponents, count = getComponents(forest[v][i], forest, count)

                #Add those child to component
                vertexesInComponent = vertexesInComponent + vertexesInChildComponents

                #If we have even number of vertexes in this component
                if vertexesInChildComponents % 2 == 0:

                    #We can cut this edge
                    count = count + 1

        #Return how much vertexes we have in component
        #and how much edges we can cut
        return vertexesInComponent, count

components, count = getComponents(0, forest, count)
print(count)
