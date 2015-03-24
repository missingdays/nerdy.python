n = int(input().split()[1])

forest = [None] * (n + 1)

visited = []

for i in range(len(forest)):
    forest[i] = []

for i in range(n):

    edge = list(map(int, input().split()))

    forest[edge[0] - 1].append(edge[1] - 1)
    forest[edge[1] - 1].append(edge[0] - 1)

count = 0

def getComponents(v, forest, count):

    if not v in visited:

        components = 1

        visited.append(v)

        for i in range(len(forest[v])):

            if not forest[v][i] in visited:

                childComponents, count = getComponents(forest[v][i], forest, count)

                components = components + childComponents

                if childComponents % 2 == 0:
                    count = count + 1

        return components, count
components, count = getComponents(0, forest, count)
print(count)
