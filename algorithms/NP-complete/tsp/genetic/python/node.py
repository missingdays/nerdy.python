
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

    def distance_to(self, node):
        return sqrt( (node.x - self.x)**2 + (node.y - self.y)**2 )
