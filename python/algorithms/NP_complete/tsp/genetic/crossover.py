
import random

from node_map import *

__all__ = ["CXCrossover", "orderedCrossover"]

def CXCrossover(nodeMap1, nodeMap2):

    nodes = [None for i in range(len(nodeMap1))]

    cycle = findCycle(nodeMap1, nodeMap2)

    for index in cycle:
        nodes[index] = nodeMap1.nodes[index]

    for i in range(len(nodeMap1)):
        if nodes[i] == None:
            nodes[i] = nodeMap2.nodes[i]

    return NodeMap(nodes)

def orderedCrossover(node_map_1, node_map_2):

    nodes = [None for i in range(len(node_map_1))]

    start = random.randint(0, len(node_map_1)-1)
    end = random.randint(0, len(node_map_1)-1)

    start = min(start, end)
    end = max(start, end)


    added_nodes = set()

    for i in range(start, end+1):
        nodes[i] = node_map_1.nodes[i]
        added_nodes.add(nodes[i].id)

    current_index = (end+1) % len(node_map_1)

    for i in range(current_index, 2*len(node_map_2)):

        real_index = i%len(node_map_2)

        if node_map_2.nodes[real_index].id not in added_nodes:
            nodes[current_index] = node_map_2.nodes[real_index]
            added_nodes.add(nodes[current_index].id)

            current_index += 1
            current_index %= len(node_map_2)


    return NodeMap(nodes)

def findCycle(nodeMap1, nodeMap2):
    seenIndexes = set()

    currentIndex = 0

    while currentIndex not in seenIndexes:
        seenIndexes.add(currentIndex)

        currentIndex = nodeMap2.getNodeIndex(nodeMap1.nodes[currentIndex])

    return seenIndexes
