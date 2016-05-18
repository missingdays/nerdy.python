
from crossover import *
from tsp_solver import *

__all__ = ["getBestPartSelection", "getRouletteSelection"]

def getBestPartSelection(crossover=CXCrossover, gensToSurvive=0.5):
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

def getRouletteSelection(crossover=CXCrossover):

    def rouletteSelection(population):

        selectedPopulation = selectPopulationBasedOnFitness(population)

        newPopulation = createNewPopulation(selectedPopulation, crossover)

        return newPopulation

    return rouletteSelection

def selectPopulationBasedOnFitness(population):
    selectedPopulation = []

    for i in range(len(population)):
        selectedPopulation.append(selectGenBasedOnFitness(population))

    return selectedPopulation

def selectGenBasedOnFitness(population):
    fitnessSum = 0

    for gen in population:
        fitnessSum += TSPSolver.fitness(gen)

    rand = random.random() * fitnessSum

    for gen in population:
        rand -= TSPSolver.fitness(gen)

        if rand <= 0:
            return gen

    # In case of rounding error
    return population[len(population)-1]

def createNewPopulation(population, crossover):
    newPopulation = []

    sizeOfPopulation = len(population)

    while len(newPopulation) < sizeOfPopulation:
        i = random.randint(0, sizeOfPopulation-1)
        j = random.randint(0, sizeOfPopulation-1)

        newPopulation.append(crossover(population[i], population[j]))

    return newPopulation
