
class Node:

    __slots__ = ["key", "value", "next"]

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
