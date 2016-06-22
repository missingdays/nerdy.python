
from . import LinkedList

def test_linked_list_add_key():

    l = LinkedList()

    l.add(0)
    assert l.head.key == 0

    l = LinkedList()
    n = 100

    for i in range(n):
        l.add(i)

    assert len(l) == n

    for i in range(n):
        assert l.find(i) == None

def test_linked_list_add_value():

    l = LinkedList()

    l.add(0, 0)
    assert l.head.key == 0
    assert l.head.value == 0

    l = LinkedList()
    n = 100

    for i in range(n):
        l.add(i, n-i)

    assert len(l) == n

    for i in range(n):
        assert l.find(i) == n - i


def test_linked_list_set():

    l = LinkedList()
    l.add(0, 0)
    l.set(0, 1)

    assert l.head.key == 0
    assert l.head.value == 1

    l = LinkedList()

    n = 100

    for i in range(n):
        l.add(i, i)

    for i in range(n):
        l.set(i, n-i-1)

    for i in range(n):
        assert l.find(i) == n-i-1

def test_linked_list_remove():

    l = LinkedList()

    assert l.remove(0) == False

    l.add(1)
    assert l.remove(1) == True

    assert len(l) == 0

    n = 100

    for i in range(n):
        l.add(i)

    for i in range(n):
        assert l.remove(i) == True

    assert len(l) == 0

    for i in range(n):
        l.add(i)

    for i in range(n):
        assert l.remove(n-i-1) == True

    assert len(l) == 0

    for i in range(n):
        l.add(i)

    for i in range(n//2, n):
        assert l.remove(i) == True

    for i in range(n//2):
        assert l.remove(i) == True