'''
    type: structure
    theme: collections
    sub-theme: sets
    name: set
    author of code: Evgeny @missingdays Bovykin

'''

class Set:

    def __init__(self):
        self.keys = {}

    def add(self, value):
        self.keys[value] = 0 # use any dummy value here

    def has(self, value):
        return value in self.keys

    def __contains__(self, value):
        return self.has(value)

    def remove(self, value):
        del self.keys[value]


if __name__ == "__main__":

    s = Set()

    s.add(1)
    s.add(2)
    s.add(3)

    assert 1 in s
    assert 2 in s
    assert 3 in s
    assert 4 not in s

    s.remove(1)

    assert 1 not in s

    s.add(1)

    assert 1 in s

    print("Set python done")
