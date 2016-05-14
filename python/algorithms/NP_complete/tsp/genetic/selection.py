
from crossover import *
from tsp_genetic import *

def getBestPartSelection(gensToSurvive=0.5, crossover=CXCrossover):
    def bestPartSelection(population):

        sizeOfPopulation = len(population)

        population = TSPSolver.sortGensByFitness(population)

        numberOfBest = int(sizeOfPopulation * gensToSurvive)
        numberOfWorst = sizeOfPopulation - numberOfBest

        population = population[numberOfWorst:]

        size = len(population)

        while len(population) < sizeOfPopulation:
            n1 = random.randint(0, size-1)
            n2 = random.randint(0, size-1)

            child = crossover(population[n1], population[n2])

            population.append(child)

        return population

    return bestPartSelection
