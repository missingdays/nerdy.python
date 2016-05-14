
import random
import time

from node import Node
from node_map import NodeMap
from crossover import *
from selection import *

random.seed(time.time())

class TSPSolver:

    def __init__(self, gensToSurvive=0.5, sizeOfPopulation=10, numberOfCycles=100, 
            mutationProbability=0.02, targetNodeMap=None, crossover=CXCrossover, 
            selection=None):
        self.gensToSurvive = gensToSurvive
        self.sizeOfPopulation = sizeOfPopulation
        self.numberOfCycles = numberOfCycles
        self.mutationProbability = mutationProbability
        self.targetNodeMap = targetNodeMap
        self.crossover = crossover

        if selection == None:
            self.selection = getBestPartSelection(crossover=crossover)
        else:
            self.selection = selection

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

            print("TSPSolver running with parameters: ")
            print("Gens to survive = " + str(self.gensToSurvive))

            print("Target node map is ")
            print(str(self.targetNodeMap))

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
                print("Cycle " + str(index))
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
    nodes = []

    j = 1
    for i in range(50):
        nodes.append(Node(i+j, i+j, i))

    nodeMap = NodeMap(nodes)

    tspSolver = TSPSolver()
    tspSolver.setTargetNodeMap(nodeMap)
    tspSolver.mutationProbability = 0.01
    tspSolver.gensToSurvive = 0.3
    tspSolver.sizeOfPopulation = 1000
    tspSolver.numberOfCycles = 20000

    tspSolver.debug = True

    tspSolver.solve()

    bestNodeMap = tspSolver.getBestNodeMap()

    print("Best plate is")
    print(bestNodeMap)
    print("It's distance is ", bestNodeMap.getOverallDistance())
    print("Target nodeMap distance was ", nodeMap.getOverallDistance())


if __name__ == "__main__":
    main()
