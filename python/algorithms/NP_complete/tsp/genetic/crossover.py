
from node_map import *

__all__ = ["CXCrossover"]

def CXCrossover(nodeMap1, nodeMap2):
    nodes = []

    for i in range(len(nodeMap1)):
        nodes.append(None)

    cycle = NodeMap.findCycle(nodeMap1, nodeMap2)

    for index in cycle:
        nodes[index] = nodeMap1.nodes[index]

    for i in range(len(nodeMap1)):
        if nodes[i] == None:
            nodes[i] = nodeMap2.nodes[i]

    return NodeMap(nodes)
