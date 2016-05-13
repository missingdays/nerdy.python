
import random
import time

from node import Node
from node_map import NodeMap

random.seed(time.time())

class TSPSolver:

    def __init__(self, gensToSurvive=0.5, sizeOfPopulation=10, numberOfCycles=100, mutationProbability=0.02, targetNodeMap=None):
        self.gensToSurvive = gensToSurvive
        self.sizeOfPopulation = sizeOfPopulation
        self.numberOfCycles = numberOfCycles
        self.mutationProbability = mutationProbability
        self.targetNodeMap = targetNodeMap

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
        self.leaveBestOfGens()
        self.produceNewGens()
        self.performMutate()

    def leaveBestOfGens(self):
        self.sortGensByFitness()

        numberOfBest = int(self.sizeOfPopulation * self.gensToSurvive)
        numberOfWorst = len(self.population) - numberOfBest

        self.population = self.population[numberOfWorst:]

    def produceNewGens(self):

        size = len(self.population)
        newPopulation = self.population

        while len(newPopulation) < self.sizeOfPopulation:
            n1 = random.randint(0, size-1)
            n2 = random.randint(0, size-1)

            child = self.population[n1].crossover(self.population[n2])

            newPopulation.append(child)

        self.population = newPopulation

    def performMutate(self):
        for gen in self.population:
            gen.mutate(self.mutationProbability)

    def sortGensByFitness(self):
        self.population.sort(key=lambda gen: TSPSolver.fitness(gen))

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
        self.sortGensByFitness()

        return self.population[len(self.population) - 1]

    def setTargetNodeMap(self, nodeMap):
        self.targetNodeMap = nodeMap

    @staticmethod
    def fitness(gen):
        return 1 / gen.getOverallDistance()


def main():
    nodes = []

    j = 1
    for i in range(30):
        nodes.append(Node(i+j, i+j, i))

    nodeMap = NodeMap(nodes)

    tspSolver = TSPSolver()
    tspSolver.setTargetNodeMap(nodeMap)
    tspSolver.sizeOfPopulation = 100
    tspSolver.numberOfCycles = 10000

    tspSolver.debug = True

    tspSolver.solve()

    bestNodeMap = tspSolver.getBestNodeMap()

    print("Best plate is")
    print(bestNodeMap)
    print("It's distance is ", bestNodeMap.getOverallDistance())
    print("Target nodeMap distance was ", nodeMap.getOverallDistance())


if __name__ == "__main__":
    main()
