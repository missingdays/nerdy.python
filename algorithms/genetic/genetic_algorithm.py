
class GeneticAlgorithm:

    def __init__(self, *, population_size=10, number_of_cycles=100, 
        mutation_probability=0.01, random_first_population=True, fitness_function=None, crossover=None, 
        selection=None, mutation=None, gen_generator=None):
    
        self.population_size = population_size
        self.number_of_cycles = number_of_cycles
        self.mutation_probability = mutation_probability
        self.random_first_population = random_first_population

        self.fitness_function = fitness_function
        self.crossover = crossover
        self.selection = selection
        self.mutation = mutation
        self.gen_generator = gen_generator

        self.population = []

    def __iter__(self):
        self.generate_first_population()

        self.current_cycle = 0

        return self

    def __next__(self):
        if self.current_cycle >= self.number_of_cycles:
            raise StopIteration()

        self.current_cycle += 1

        return self.perform_cycle(), self.current_cycle

    def generate_first_population(self):
        
        if self.gen_generator == None:
            raise Exception("Set gen generator before performing evolution")

        for _ in range(self.population_size):
            if self.random_first_population:
                self.population.append(self.gen_generator.random())
            else:
                self.population.append(self.gen_generator.new())

    def perform_cycle(self):
        pass
