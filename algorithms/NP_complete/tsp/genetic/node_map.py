import random
import time

from node import Node
from mutation import *

random.seed(time.time())

class NodeMap:

    def __init__(self, nodes):
        self.nodes = []

        self.distance = None
        self.mutation = None

        for node in nodes:
            self.nodes.append(node.copy())

    def copy(self):
        cp = NodeMap(self.nodes)
        cp.mutation = self.mutation
        cp.distance = self.distance
        
        return cp

    def add_node(self, node):
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

    def get_overall_distance(self):

        if self.distance != None:
            return self.distance

        distance = 0

        for i in range(len(self.nodes) - 1):
            distance += self.nodes[i].distance_to(self.nodes[i+1])

        # Cycle
        distance += self.nodes[0].distance_to(self.nodes[len(self.nodes)-1])

        self.distance = distance

        return distance

    def shuffle(self):
        random.shuffle(self.nodes)

        self.distance = None

    def mutate(self, mutation, mutation_probability):
        mutation(self.nodes, mutation_probability)
        self.distance = None

    def get_node_index(self, node_to_find):
        id_to_find = node_to_find.id

        for index, node in enumerate(self.nodes):
            if node.id == id_to_find:
                return index

        raise Exception("Couldn't find node " +  str(node_to_find) + " in " + str(self))

def main():
    pass

if __name__ == "__main__":
    main()
