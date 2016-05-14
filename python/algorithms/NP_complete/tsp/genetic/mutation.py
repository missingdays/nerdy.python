
import random

__all__ = ["neighbourSwapMutation", "randomSwapMutation"]

def neighbourSwapMutation(nodes, mutationProbability):
    for i in range(len(nodes)-1):
        if random.random() < mutationProbability:
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]

def randomSwapMutation(nodes, mutationProbability):
    for i in range(len(nodes)):
        if random.random() < mutationProbability:
            j = random.randint(0, len(nodes)-1)

            nodes[i], nodes[j] = nodes[j], nodes[i]

def randomInsertMutation(nodes, mutationProbability):
    for i in range(len(nodes)):
        if random.random() < mutationProbability:

            # Index to insert after
            j = random.randint(0, len(nodes)-2)


