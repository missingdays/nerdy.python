
import random
import time

from node import Node

random.seed(time.time())

class NodeMap:

    def __init__(self, nodes):
        self.nodes = []

        for node in nodes:
            self.nodes.append(node.copy())

    def copy(self):
        return NodeMap(self.nodes)

    def addNode(self, node):
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        s = ""

        for node in self.nodes:
            s += str(node)
            s += "\n"

        return s

    def getOverallDistance(self):

        distance = 0

        for i in range(len(self.nodes) - 1):
            distance += self.nodes[i].distanceTo(self.nodes[i+1])

        return distance

    def shuffle(self):
        random.shuffle(self.nodes)

    def mutate(self, mutationProbability):
        self.weakMutate(mutationProbability)

    def hardMutate(self):
        mutations = 10

        for i in range(mutations):
            self.weakMutate()

    def weakMutate(self, mutationProbabilty):
        for i in range(len(self.nodes)):
            if random.random() < mutationProbabilty:
                j = random.randint(0, len(self.nodes)-1)

                self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

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

        while currentIndex not in seenIndexes:
            seenIndexes.add(currentIndex)

            currentIndex = nodeMap2.getNodeIndex(nodeMap1.nodes[currentIndex])

        return seenIndexes

    def getNodeIndex(self, nodeToFind):
        idToFind = nodeToFind.id

        for index, node in enumerate(self.nodes):
            if node.id == idToFind:
                return index


def main():
    pass

if __name__ == "__main__":
    main()
