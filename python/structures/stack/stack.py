'''
    type: structure
    theme: collections
    sub-theme: arrays
    name: stack
    author of code: Evgeny @missingdays Bovykin

'''

class Stack():


    def __init__(self, size):

        #Array where we will store our values
        self._array = [0] * size

        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def push(self, value):
        self.top = self.top + 1

        self._array[self.top - 1] = value

    def pop(self):

        if not self.isEmpty():
            self.top = self.top - 1

            return self._array[self.top]

#Create new stack
stack = Stack(3)

#Push some values
stack.push(5)
stack.push(6)
stack.push(0)

#Pop them back
print(stack.pop()) #0
print(stack.pop()) #6
print(stack.pop()) #5
