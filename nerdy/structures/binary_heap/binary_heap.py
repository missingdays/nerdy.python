'''
    type: structure
    theme: trees
    sub-theme: storing and searching
    name: binary heap
    author of code: Evgeny @missingdays Bovykin

'''

def buildHeap(A):
    for start in range((len(A) - 2) / 2, -1, -1):
        heapify(A, start, len(A) - 1)


def heapify(A, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and A[child] < A[child + 1]:
            child += 1
        if child <= end and A[root] < A[child]:
            A[root], A[child] = A[child], A[root]
            root = child
        else:
            return
