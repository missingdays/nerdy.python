
"""
Implements diffrenet mutation on permutations.
Every mutation takes nodes and mutationProbability as arguments.
Mutation probabilty defines probability of a single node to be mutated (moved, swaped with another node etc).
"""
import random

__all__ = ["neighbourSwapMutation", "randomSwapMutation", "randomInsertMutation"]

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
