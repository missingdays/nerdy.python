
from crossover import *
from tsp_solver import *

__all__ = ["get_best_part_selection", "get_roulette_selection", "get_mean_fitness_selection"]

def get_best_part_selection(crossover=cyclic_crossover, gens_to_survive=0.5):
    def best_part_selection(population):

        population_size = len(population)

        population = TSPSolver.sort_gens_by_fitness(population)

        number_of_best = int(population_size * gens_to_survive)
        number_of_worst = population_size - number_of_best

        population = population[number_of_worst:]

        size = len(population)

        while len(population) < population_size:
            n1 = random.randint(0, size-1)
            n2 = random.randint(0, size-1)

            child = crossover(population[n1], population[n2])

            population.append(child)

        return population

    return best_part_selection

def get_roulette_selection(crossover=cyclic_crossover):

    def roulette_selection(population):

        selected_population = select_population_based_on_fitness(population)

        new_population = create_new_population(selected_population, crossover)

        return new_population

    return roulette_selection

def get_mean_fitness_selection(crossover=cyclic_crossover):

    def mean_fitness_selection(population):

        selected_population = select_population_better_than_mean(population)
        
        new_population = create_new_population(selected_population, crossover, population_size=len(population))

        return new_population

    return mean_fitness_selection

def select_population_based_on_fitness(population):
    selected_population = []

    for i in range(len(population)):
        selected_population.append(select_gen_based_on_fitness(population))

    return selected_population

def select_population_better_than_mean(population):

    mean_fitness = get_mean_fitness(population)

    selected_population = [gen for gen in population if TSPSolver.fitness(gen) >= mean_fitness]

    return selected_population

def select_gen_based_on_fitness(population):
    fitness_sum = 0

    for gen in population:
        fitness_sum += TSPSolver.fitness(gen)

    rand = random.random() * fitness_sum

    for gen in population:
        rand -= TSPSolver.fitness(gen)

        if rand <= 0:
            return gen

    # In case of rounding error
    return population[len(population)-1]

def create_new_population(population, crossover, population_size=None):
    new_population = []

    if population_size == None:
        population_size = len(population)

    while len(new_population) < population_size:
        i = random.randint(0, len(population)-1)
        j = random.randint(0, len(population)-1)

        new_population.append(crossover(population[i], population[j]))

    return new_population

def get_mean_fitness(population):

    s = sum(TSPSolver.fitness(gen) for gen in population)

    return s / len(population)
