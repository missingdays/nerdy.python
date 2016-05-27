
"""
Implements diffrenet mutation on permutations.
Every mutation takes nodes and mutation_probability as arguments.
Mutation probabilty defines probability of a single node to be mutated (moved, swaped with another node etc).
"""

import random

__all__ = ["neighbour_swap_mutation", "random_swap_mutation", "random_insert_mutation", "random_reflect_segment_mutation",
        "shuffle_segment_mutation", "shuffle_random_pieces_mutation"]

def neighbour_swap_mutation(nodes, mutation_probability):
    """
    O(n) mutation
    """
    for i in range(len(nodes)-1):
        if random.random() < mutation_probability:
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]

def random_swap_mutation(nodes, mutation_probability):
    """
    O(n) mutation
    """
    for i in range(len(nodes)):
        if random.random() < mutation_probability:
            j = random.randint(0, len(nodes)-1)

            nodes[i], nodes[j] = nodes[j], nodes[i]

def random_insert_mutation(nodes, mutation_probability):
    """
    O(n^2) mutation
    """
    for i in range(len(nodes)):
        if random.random() < mutation_probability:

            # Index to insert before
            j = -1

            while j == i:
                j = random.randint(1, len(nodes)-1)

            nodes.insert(j, nodes.pop(i))

def random_reflect_segment_mutation(nodes, mutation_probability):
    """
    O(n^2) mutation
    """

    # How long can reflected part be
    # e.g. 0.25 means reflected part length can't be bigger than 25% of nodes length
    max_part_len = 0.05
    max_part_elems = len(nodes) * max_part_len

    for i in range(len(nodes)):
        if random.random() < mutation_probability:

            part_elems = int(max_part_elems * random.random())

            if part_elems < 2:
                part_elems = 2

            change_segment(nodes, i, part_elems, reversed)


def shuffle_segment_mutation(nodes, mutation_probability):
    """
    O(n^2) mutation
    """

    # How long can shuffled part be
    # e.g. 0.25 means shuffled part length can't be bigger than 25% of nodes length
    max_part_len = 0.05
    max_part_elems = len(nodes) * max_part_len

    for i in range(len(nodes)):
        if random.random() < mutation_probability:

            part_elems = int(max_part_elems * random.random())

            if part_elems < 2:
                part_elems = 2

            change_segment(nodes, i, part_elems, shuffled)

def shuffle_random_pieces_mutation(nodes, mutation_probability):
    """
    O(n^2) mutation

    Shuffles random nodes. Chooses their indexes based on mutation_probability multiplied by some coefficient.
    Coefficient is tuned so that algorithms shuffles more than random_swap_mutation but doesn't shuffle too much at the same time
    """

    coeff = 0.5

    # How many nodes we will take for shuffling
    # e.g. 0.25 means we will take 25% of nodes to shuffle
    max_pieces_number = min(7, 0.05 * len(nodes))

    # We need this so we don't end up selection only first half or so nodes
    # and ignoring the rest.
    start_position = int(random.random() * len(nodes))

    nodes_to_shuffle = {}

    for j in range(len(nodes)):
        i = (j + start_position) % len(nodes)

        if random.random() < mutation_probability * coeff:
            if len(nodes_to_shuffle) < max_pieces_number:
                nodes_to_shuffle[i] =  nodes[i]

    shuffled_nodes = shuffled_dict(nodes_to_shuffle)

    for i, node in shuffled_nodes.items():
        nodes[i] = node

def shuffled(x):
    return random.sample(x, len(x))

def shuffled_dict(x):
    keys = x.keys()
    values = shuffled(list(x.values()))

    return dict(zip(keys, values))

def change_segment(nodes, i, length, function):
    if i + length >= len(nodes):
        nodes[i-length:i] = function(nodes[i-length:i])
    elif i - length < 0:
        nodes[i:i+length] = function(nodes[i:i+length])
    elif random.random() < 0.5:
        nodes[i-length:i] = function(nodes[i-length:i])
    else:
        nodes[i:i+length] = function(nodes[i:i+length])
