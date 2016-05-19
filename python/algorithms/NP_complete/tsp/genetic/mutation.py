
"""
Implements diffrenet mutation on permutations.
Every mutation takes nodes and mutationProbability as arguments.
Mutation probabilty defines probability of a single node to be mutated (moved, swaped with another node etc).
"""
import random

__all__ = ["neighbourSwapMutation", "randomSwapMutation", "randomInsertMutation", "randomReflectPartMutation",
        "shuffleSegmentMutation"]

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

def randomReflectPartMutation(nodes, mutation_probability):
    """
    O(n^2) mutation
    """

    # How long can reflected part be
    # e.g. 0.25 means reflected part length can't be bigger than 25% of nodes length
    max_part_len = 0.2
    max_part_elems = len(nodes) * max_part_len

    for i in range(len(nodes)):
        if random.random() < mutation_probability:

            part_elems = int(max_part_elems * random.random())

            if part_elems < 2:
                part_elems = 2

            change_segment(nodes, i, part_elems, reversed)


def shuffleSegmentMutation(nodes, mutation_probability):
    """
    O(n^2) mutation
    """

    # How long can shuffled part be
    # e.g. 0.25 means shuffled part length can't be bigger than 25% of nodes length
    max_part_len = 0.1
    max_part_elems = len(nodes) * max_part_len

    for i in range(len(nodes)):
        if random.random() < mutation_probability:

            part_elems = int(max_part_elems * random.random())

            if part_elems < 2:
                part_elems = 2

            change_segment(nodes, i, part_elems, shuffled)

def shuffled(x):
    return random.sample(x, len(x))

def change_segment(nodes, i, length, function):
    if i + length >= len(nodes):
        nodes[i-length:i] = function(nodes[i-length:i])
    elif i - length < 0:
        nodes[i:i+length] = function(nodes[i:i+length])
    elif random.random() < 0.5:
        nodes[i-length:i] = function(nodes[i-length:i])
    else:
        nodes[i:i+length] = function(nodes[i:i+length])
