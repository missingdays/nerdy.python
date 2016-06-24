
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
        """
        Returns next permutation

        permutation.next().rank() always equals (permutation.rank() + 1) % factorial(N) where N is the length of permutation
        """
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

    def rank(self):
        """
        Returns rank of a current permutation

        Time: O(n^2)
        Space: O(1)
        """

        l = len(self)
        mul = factorial(l)
        rank = 0

        for i, number in enumerate(self):
            mul //= (l - i)

            smaller_on_right = 0

            for right_number in self[i+1:]:
                if right_number < number:
                    smaller_on_right += 1

            rank += smaller_on_right * mul

        return rank
   
    @classmethod
    def from_rank(cls, *, n=-1, rank=0):
        """
        Returns new permutation that has given rank

        Time: O(n^2)
        Space: O(n)
        """

        if n < 0:
            raise ValueError("Permutation length must be atleast 0")

        if rank < 0:
            raise ValueError("Permutation rank can't be negative")

        permutation, tmp_permutation = cls(n), [i for i in range(1, n+1)]

        current_index = 0

        while len(tmp_permutation) > 0:
            size = factorial(len(tmp_permutation) - 1)
            index = rank // size

            permutation[current_index] = tmp_permutation[index]

            tmp_permutation = (index > 0 and tmp_permutation[:index] or []) + (index < len(tmp_permutation)-1 and tmp_permutation[index+1:] or [])

            rank %= size

            current_index += 1

        return permutation

    def equal(self, another):
        """
        Returns whether self permutation equals to another permutation
        Two permutations are equal, if they have the same length (e.g. the both contain numbers from 1 to some N)
        and all their elements come in the same order
        """

        if len(self) != len(another):
            return False

        for e1, e2 in zip(self, another):
            if e1 != e2:
                return False

        return True

    def __eq__(self, another):
        return self.equal(another)

    def __ne__(self, another):
        return not self.equal(another)

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
        Please note, that you shouldn't typicaly set items by yourself unless you 
        totaly know what you are doing, as setting wrong numbers can break all functionality
        """
        self.numbers[i] = v

    def __getitem__(self, i):
        return self.numbers[i]

    def __reversed__(self):
        return reversed(self.numbers)

    def __contains__(self, item):
        return item in self.numbers
