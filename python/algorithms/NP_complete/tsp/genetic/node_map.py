import random
import time

from node import Node
from mutation import *

random.seed(time.time())

class NodeMap:

    def __init__(self, nodes, mutation=randomInsertMutation):
        self.nodes = []

        self.distance = None
        self.mutation = mutation

        for node in nodes:
            self.nodes.append(node.copy())

    def copy(self):
        return NodeMap(self.nodes)

    def addNode(self, node):
        self.nodes.append(node)

        self.distance = None

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        s = ""

        for node in self.nodes:
            s += str(node)
            s += "\n"

        return s

    def getOverallDistance(self):

        if self.distance != None:
            return self.distance

        distance = 0

        for i in range(len(self.nodes) - 1):
            distance += self.nodes[i].distanceTo(self.nodes[i+1])

        self.distance = distance

        return distance

    def shuffle(self):
        random.shuffle(self.nodes)

        self.distance = None

    def mutate(self, mutationProbability):
        self.mutation(self.nodes, mutationProbability)

        self.distance = None

    def getNodeIndex(self, nodeToFind):
        idToFind = nodeToFind.id

        for index, node in enumerate(self.nodes):
            if node.id == idToFind:
                return index

        raise Exception("Couldn't find node " +  str(nodeToFind) + " at " + str(self))

def main():
    pass

if __name__ == "__main__":
    main()
