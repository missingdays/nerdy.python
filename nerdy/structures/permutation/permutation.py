
from math import factorial

class Permutation(list):
    """
    Permutation is some arragment of numbers from 1 to N
    """

    def __init__(self, n):
        self.n = n
        self.numbers = [i for i in range(1, n+1)]

    def copy(self):
        cp = Permutation(self.n)
        cp.numbers = list(self.numbers)

        return cp

    def next(self):
        i = len(self) - 1

        while i > 0 and self[i-1] >= self[i]:
            i -= 1

        if i <= 0:
            return Permutation(self.n)

        new_permutation = self.copy()

        j = len(new_permutation) - 1
        while new_permutation[j] <= new_permutation[i-1]:
            j -= 1

        new_permutation[i-1], new_permutation[j] = new_permutation[j], new_permutation[i-1]

        new_permutation[i:] = new_permutation[len(new_permutation)-1:i-1:-1]

        return new_permutation

    """
    def lex_rank(self):
        lex_rank = 0
        was = {}

        n = len(self)

        for i in range(n):
            for j in range(i):
                if j not in was:
                    lex_rank += factorial(n-i)
            was[self[i]] = True

        return lex_rank
    """

    def __str__(self):
        return str(self.numbers)

    def __repr__(self):
        return repr(self.numbers)

    def __iter__(self):
        return iter(self.numbers)

    def __len__(self):
        return len(self.numbers)

    def __setitem__(self, i, v):
        """
        Please note, that you should typicaly set items by yourself unless you 
        totaly know what you are doing, as setting wrong numbers can break all functionality
        """
        self.numbers[i] = v

    def __getitem__(self, i):
        return self.numbers[i]
