
from math import sqrt

'''
2d node
'''
class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def copy(self):
        return Node(self.x, self.y, self.id)

    def distanceTo(self, node):
        return sqrt( (node.x - self.x)**2 + (node.y - self.y)**2 )

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"
