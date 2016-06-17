
import random 
import time

from node import Node
from node_map import NodeMap
from crossover import *
from selection import *
from mutation import *

random.seed(time.time())

class TSPSolver:

    def __init__(self, population_size=10, number_of_cycles=100, 
            mutation_probability=0.01, target_node_map=None, crossover=cyclic_crossover, 
            selection_getter=None, mutation=shuffle_segment_mutation):
        self.population_size = population_size
        self.number_of_cycles = number_of_cycles
        self.mutation_probability = mutation_probability
        self.target_node_map = target_node_map
        self.crossover = crossover
        self.mutation = mutation

        if selection_getter == None:
            self.selection = get_best_part_selection(crossover=crossover)
        else:
            self.selection = selection_getter(crossover=crossover)

        self.population = []

        self.debug = False

    def solve(self):
        
        if self.target_node_map == None:
            raise ValueError("Target Node Map can't be None. Set it before calling solve")

        self.debug_after_cycles = self.number_of_cycles // 50

        self.before_solve()

        self.perform_solve()

        self.after_solve()

    def before_solve(self):
        if self.debug:

            print("Target node map is ")
            print(str(self.target_node_map))
            print("Its distance is " + str(self.target_node_map.get_overall_distance()))
            print("\n")

    def perform_solve(self):

        self.generate_first_population()

        for i in range(self.number_of_cycles):
            self.perform_cycle(i)

            self.after_cycle(i)

    def generate_first_population(self):

        self.population = []

        for i in range(self.population_size):
            gen = self.target_node_map.copy()

            gen.shuffle()

            self.population.append(gen)

    def perform_cycle(self, index):
        self.perform_selection()
        self.perform_mutate()

    def perform_selection(self):
        self.population = self.selection(self.population)

    def perform_mutate(self):
        for gen in self.population:
            gen.mutate(self.mutation, self.mutation_probability)

    def after_cycle(self, index):
        if self.debug:
            if index % self.debug_after_cycles == 0:
                print("Cycle " + str(index) + " of " + str(self.number_of_cycles))
                #print("Best node map is")
                #print(self.get_best_node_map())
                print("Its distance is " + str(self.get_best_node_map().get_overall_distance()))
                print("\n")

    def after_solve(self):
        pass

    def get_best_node_map(self):
        self.population = TSPSolver.sort_gens_by_fitness(self.population)

        return self.population[len(self.population) - 1]

    @staticmethod
    def fitness(gen):
        return 1 / gen.get_overall_distance()

    @staticmethod
    def sort_gens_by_fitness(gens):
        gens.sort(key=lambda gen: TSPSolver.fitness(gen))
        return gens

def main():
    
    node_map = generate_line(160)

    tspSolver = TSPSolver(selection_getter=get_mean_fitness_selection, crossover=ordered_crossover, 
            mutation=shuffle_random_pieces_mutation)
    tspSolver.target_node_map = node_map
    tspSolver.mutation_probability = 0.005
    tspSolver.population_size = 10000
    tspSolver.number_of_cycles = 40000

    tspSolver.debug = True

    tspSolver.solve()

    bestNodeMap = tspSolver.get_best_node_map()

    print("Best plate is")
    print(bestNodeMap)
    print("It's distance is ", bestNodeMap.get_overall_distance())
    print("Target node_map distance was ", node_map.get_overall_distance())

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
