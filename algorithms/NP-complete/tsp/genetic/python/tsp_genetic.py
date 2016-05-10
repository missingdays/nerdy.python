
from node import Node
from node_map import NodeMap

class TSPSolver:

    def __init__(self, gensToSurvive=0.1, sizeOfPopulation=10, numberOfCycles=100, mutationProbabilty=0.1):
        self.gensToSurvive = gensToSurvive
        self.sizeOfPopulation = sizeOfPopulation
        self.numberOfCycles = numberOfCycles
        self.mutationProbabilty = mutationProbabilty
