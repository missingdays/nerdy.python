
from crossover import *
from tsp_solver import *

__all__ = ["getBestPartSelection", "getRouletteSelection", "getMeanFitnessSelection"]

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

def getMeanFitnessSelection(crossover=CXCrossover):

    def mean_fitness_selection(population):

        selected_population = select_population_better_than_mean(population)
        
        new_population = createNewPopulation(selected_population, crossover, population_size=len(population))

        return new_population

    return mean_fitness_selection

def selectPopulationBasedOnFitness(population):
    selectedPopulation = []

    for i in range(len(population)):
        selectedPopulation.append(selectGenBasedOnFitness(population))

    return selectedPopulation

def select_population_better_than_mean(population):

    mean_fitness = get_mean_fitness(population)

    selected_population = [gen for gen in population if TSPSolver.fitness(gen) >= mean_fitness]

    return selected_population

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

def createNewPopulation(population, crossover, population_size=None):
    newPopulation = []

    if population_size == None:
        population_size = len(population)

    while len(newPopulation) < population_size:
        i = random.randint(0, len(population)-1)
        j = random.randint(0, len(population)-1)

        newPopulation.append(crossover(population[i], population[j]))

    return newPopulation

def get_mean_fitness(population):

    s = sum(TSPSolver.fitness(gen) for gen in population)

    return s / len(population)
