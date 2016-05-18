
"""
Implements diffrenet mutation on permutations.
Every mutation takes nodes and mutationProbability as arguments.
Mutation probabilty defines probability of a single node to be mutated (moved, swaped with another node etc).
"""
import random

__all__ = ["neighbourSwapMutation", "randomSwapMutation", "randomInsertMutation", "randomReflectPartMutation"]

def neighbourSwapMutation(nodes, mutationProbability):
    """
    O(n) mutation
    """
    for i in range(len(nodes)-1):
        if random.random() < mutationProbability:
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]

def randomSwapMutation(nodes, mutationProbability):
    """
    O(n) mutation
    """
    for i in range(len(nodes)):
        if random.random() < mutationProbability:
            j = random.randint(0, len(nodes)-1)

            nodes[i], nodes[j] = nodes[j], nodes[i]

def randomInsertMutation(nodes, mutationProbability):
    """
    O(n^2) mutation
    """
    for i in range(len(nodes)):
        if random.random() < mutationProbability:

            # Index to insert before
            j = -1

            while j == i:
                j = random.randint(1, len(nodes)-1)

            nodes.insert(j, nodes.pop(i))

def randomReflectPartMutation(nodes, mutation_probabilty):
    """
    O(n^2) mutation
    """

    # How long can reflected part be
    # e.g. 0.25 means reflected part length can't be bigger than 25% of nodes length
    max_part_len = 0.2
    max_part_elems = len(nodes) * max_part_len

    for i in range(len(nodes)):
        if random.random() < mutation_probabilty:

            part_elems = int(max_part_elems * random.random())

            if part_elems < 2:
                part_elems = 2

            if random.random() < 0.5:
                nodes[i:i+part_elems] = reversed(nodes[i:i+part_elems])
            else:
                nodes[i-part_elems:i] = reversed(nodes[i-part_elems:i])
