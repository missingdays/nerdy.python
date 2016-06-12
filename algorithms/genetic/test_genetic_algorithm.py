
from genetic_algorithm import GeneticAlgorithm
from test_utils import *

gen_generator = GenGenerator()

def test_genetic_algorithm_runs_given_number_of_times():
    number_of_cycles = 100
    genetic_algorithm = GeneticAlgorithm(number_of_cycles=number_of_cycles, gen_generator=gen_generator)

    count = 0

    for best_gen, current_cycle in genetic_algorithm:
        count += 1

        assert count == current_cycle

    assert count == number_of_cycles
