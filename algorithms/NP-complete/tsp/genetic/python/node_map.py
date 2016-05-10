
import random
import time

random.seed(time.time())

class NodeMap:

    def __init__(self, nodes):
        self.nodes = []

        for node in nodes:
            self.nodes.append(node.copy())

    def addNode(self, node):
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

    def getOverallDistance(self):

        distance = 0

        for i in range(len(nodes) - 1):
            distance += self.nodes[i].distanceTo(self.nodes[i+1])

        return distance

    def shuffle(self):
        random.shuffle(self.nodes)

    def mutate(self):
        self.hardMutate()

    def hardMutate(self):
        mutations = 10

        for i in range(mutations):
            self.weakMutate()

    def weakMutate(self):
        i = random.randint(0, len(self.nodes) - 2) # not including last element

        self.nodes[i], self.nodes[i+1] = self.nodes[i+1], self.nodes[i]

    '''
    Produces new child based on self and nodeMap.
    Uses cycle crossover
    '''
    def crossover(self, nodeMap):
        nodes = []

        for i in range(len(self)):
            nodes.append(None)

        cycle = NodeMap.findCycle(self, nodeMap)

        for index in cycle:
            nodes[index] = self.nodes[index]

        for i in range(len(self)):
            if nodes[i] == None:
                nodes[i] = nodeMap.nodes[i]

        return NodeMap(nodes)

    @staticmethod
    def findCycle(nodeMap1, nodeMap2):
        seenIndexes = set()

        currentIndex = 0

        while currentIndex not in seedIndexes:
            seenIndexes.add(currentIndex)

            currentIndex = nodeMap2.getNodeIndex(nodeMap1.nodes[currentIndex])

        return seenIndexes

    def getNodeIndex(self, nodeToFind):
        idToFind = nodeToFind.id

        for index, node in enumerate(nodeMap2.nodes):
            if node.id == idToFind:
                return index
