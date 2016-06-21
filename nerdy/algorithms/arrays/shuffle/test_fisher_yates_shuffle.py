
from .fisher_yates_shuffle import shuffle, shuffled

def fisher_yates_shuffle():
    """
    We test that array combinations tends to normal
    by shuffling small array 
    # of permutations of 7-element array is 7! = 5040
    If we shuffle 1e9 times, each permutation should appear 1e9 / 5040 = 198,412 times. 
    """

    array_size = 7
    test_number = 1e9

    """
    Error rate is how big can error in # of permutations
    """
    error_rate = 0.02

    average_permutation = test_number // factorial(array_size)
    is_average_permutation = lambda n: abs(average_permutation - n) < average_permutation * error_rate

    

def fisher_yates_shuffled():
    """
    It should not touch original array
    Since there is a chance that array will equal shuffled(array) so we need to 
    check good number of times
    """

    n = 1000
    array = list(range(n))
    original_array = list(range(n))

    for i in range(n):
        shuffled(array)

        assert array == original_array
