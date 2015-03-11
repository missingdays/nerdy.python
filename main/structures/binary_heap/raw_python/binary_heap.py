'''
    type: structure
    theme: trees
    sub-theme: storing and searching
    name: binary heap
    author of code: Evgeny @missingdays Bovykin

'''

def buildHeap(A):

    for start in range((len(A) - 2) / 2, -1, -1):
        #Heapify from lower elements
        #since they are already heap
        heapify(A, start, len(A) - 1)


def heapify(A, start, end):
    #First node in local array is root
    root = start
    #While this local node has left child
    while root * 2 + 1 <= end:
        #Get this child
        child = root * 2 + 1
        #If there is right child and he is bigger than left child
        if child + 1 <= end and A[child] < A[child + 1]:
            #Will compare root with him
            child += 1
        #If this child exists
        #and is bigger than root
        if child <= end and A[root] < A[child]:
            #Swap this child and root
            A[root], A[child] = A[child], A[root]
            #Heapify from this child now
            root = child
        else:
            return
