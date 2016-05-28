
import random

from node_map import *

__all__ = ["cyclic_crossover", "ordered_crossover"]

def cyclic_crossover(node_map_1, node_map_2):

    nodes = [None for i in range(len(node_map_1))]

    cycle = find_cycle(node_map_1, node_map_2)

    for index in cycle:
        nodes[index] = node_map_1.nodes[index]

    for i in range(len(node_map_1)):
        if nodes[i] == None:
            nodes[i] = node_map_2.nodes[i]

    return NodeMap(nodes)

def ordered_crossover(node_map_1, node_map_2):

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

def find_cycle(node_map_1, node_map_2):
    seen_indexes = set()

    current_index = 0

    while current_index not in seen_indexes:
        seen_indexes.add(current_index)

        current_index = node_map_2.gen_node_index(nodeMap1.nodes[current_index])

    return seen_indexes
