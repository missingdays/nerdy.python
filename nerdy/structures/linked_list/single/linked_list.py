
from nerdy.structures import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, key, value=None):
        temp = Node(key, value, self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.next

        return count

    def __len__(self):
        return self.size()

    def find(self, key):
        current = self.head

        while current != None:
            if current.key == key:
                return current.value
            else:
                current = current.next

        raise KeyError

    def __getitem__(self, key):
        return self.find(key)

    def set(self, key, value):
        current = self.head

        while current != None:
            if current.key == key:
                current.value = value
                return
            else:
                current = current.next

        raise KeyError

    def __setitem__(self, key, value):
        return self.set(key, value)

    def remove(self, key):
        current = self.head
        previous = None

        while current != None:
            if current.key == key:
                break
            else:
                previous = current
                current = current.next
        else:
            return False

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

        return True

    def __iter__(self):
        current = self.head

        while current != None:
            yield current.key, current.value
            current = current.next

        raise StopIteration