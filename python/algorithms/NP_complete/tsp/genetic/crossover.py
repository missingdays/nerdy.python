
from node_map import *

__all__ = ["CXCrossover"]

def CXCrossover(nodeMap1, nodeMap2):
    nodes = []

    for i in range(len(nodeMap1)):
        nodes.append(None)

    cycle = findCycle(nodeMap1, nodeMap2)

    for index in cycle:
        nodes[index] = nodeMap1.nodes[index]

    for i in range(len(nodeMap1)):
        if nodes[i] == None:
            nodes[i] = nodeMap2.nodes[i]

    return NodeMap(nodes)

def findCycle(nodeMap1, nodeMap2):
    seenIndexes = set()

    currentIndex = 0

    while currentIndex not in seenIndexes:
        seenIndexes.add(currentIndex)

        currentIndex = nodeMap2.getNodeIndex(nodeMap1.nodes[currentIndex])

    return seenIndexes
