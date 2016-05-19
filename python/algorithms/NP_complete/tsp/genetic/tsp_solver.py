
import random
import time

from node import Node
from node_map import NodeMap
from crossover import *
from selection import *

random.seed(time.time())

class TSPSolver:

    def __init__(self, sizeOfPopulation=10, numberOfCycles=100, 
            mutationProbability=0.02, targetNodeMap=None, crossover=CXCrossover, 
            selectionGetter=None):
        self.sizeOfPopulation = sizeOfPopulation
        self.numberOfCycles = numberOfCycles
        self.mutationProbability = mutationProbability
        self.targetNodeMap = targetNodeMap
        self.crossover = crossover

        if selectionGetter == None:
            self.selection = getBestPartSelection(crossover=crossover)
        else:
            self.selection = selectionGetter(crossover=crossover)

        self.population = []

        self.debug = False
        

    def solve(self):
        
        if self.targetNodeMap == None:
            raise ValueError("Target Node Map can't be None. Set it before calling solve")

        self.debugAfterCycles = self.numberOfCycles // 10

        self.beforeSolve()

        self.performSolve()

        self.afterSolve()

    def beforeSolve(self):
        if self.debug:

            print("Target node map is ")
            print(str(self.targetNodeMap))
            print("Its distance is " + str(self.targetNodeMap.getOverallDistance()))
            print("\n")

    def performSolve(self):

        self.generateFirstPopulation()

        for i in range(self.numberOfCycles):
            self.performCycle(i)

            self.afterCycle(i)

    def generateFirstPopulation(self):

        self.population = []

        for i in range(self.sizeOfPopulation):
            gen = self.targetNodeMap.copy()

            gen.shuffle()

            self.population.append(gen)

    def performCycle(self, index):
        self.performSelection()
        self.performMutate()

    def performSelection(self):
        self.population = self.selection(self.population)

    def performMutate(self):
        for gen in self.population:
            gen.mutate(self.mutationProbability)

    def afterCycle(self, index):
        if self.debug:
            if index % self.debugAfterCycles == 0:
                print("Cycle " + str(index) + " of " + str(self.numberOfCycles))
                print("Best node map is")
                print(self.getBestNodeMap())
                print("Its distance is " + str(self.getBestNodeMap().getOverallDistance()))
                print("\n")

    def afterSolve(self):
        pass

    def getBestNodeMap(self):
        self.population = TSPSolver.sortGensByFitness(self.population)

        return self.population[len(self.population) - 1]

    def setTargetNodeMap(self, nodeMap):
        self.targetNodeMap = nodeMap

    @staticmethod
    def fitness(gen):
        return 1 / gen.getOverallDistance()

    @staticmethod
    def sortGensByFitness(gens):
        gens.sort(key=lambda gen: TSPSolver.fitness(gen))
        return gens

def main():
    
    nodeMap = generate_line(40)

    tspSolver = TSPSolver(selectionGetter=getBestPartSelection, crossover=orderedCrossover)
    tspSolver.setTargetNodeMap(nodeMap)
    tspSolver.mutationProbability = 0.02
    tspSolver.sizeOfPopulation = 4000
    tspSolver.numberOfCycles = 10000

    tspSolver.debug = True

    tspSolver.solve()

    bestNodeMap = tspSolver.getBestNodeMap()

    print("Best plate is")
    print(bestNodeMap)
    print("It's distance is ", bestNodeMap.getOverallDistance())
    print("Target nodeMap distance was ", nodeMap.getOverallDistance())

def generate_line(size):
    nodes = []

    for i in range(size):
        nodes.append(Node(i, i, i))

    return NodeMap(nodes)

def generate_square(size):
    nodes = []

    side = size // 4

    for i in range(side):
        nodes.append(Node(0, i, i))
    for i in range(side):
        nodes.append(Node(i, side, i+side))
    for i in range(side):
        nodes.append(Node(side, side-i, i+side*2))
    for i in range(side):
        nodes.append(Node(side-i, 0, i+side*3))

    return NodeMap(nodes)


if __name__ == "__main__":
    main()
