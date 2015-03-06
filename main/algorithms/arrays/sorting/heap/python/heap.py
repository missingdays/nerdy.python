def HeapSort(A):
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

    buildHeap(A)

    for end in range(len(A) - 1, 0, -1):
        #Place largest element from root to the end of the array
        A[end], A[0] = A[0], A[end]
        #Heapify new heap
        heapify(A, 0, end - 1)

A = [1, 2, 3, 10, 5, 9, 23, 4, 6, 6, 11, 13, 19, 0]

HeapSort(A)

for i in range(len(A)):
    print(A[i])
