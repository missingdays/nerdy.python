
from . import Node

class DoubleNode(Node):

    __slots__ = ["key", "value", "next", "prev"]

    def __init__(self, key=None, value=None, next=None, prev=None):
        super().__init__(key, value, next)
        self.prev = prev
