
import math

"""

Segment tree is handy when you need to process some kind of queries like
minimun/maximum value in a given [i, j] segment or sum of all elements in a given segment.

Code represents type of query that will be executed.
0 means we ask for sum of all values
1 means we want to find the index of the smallest number
2 means we want to find the index of the biggest number

"""

class SegmentTree:

    def __init__(self, A, code):
        self.__A = A
        self.__code = code

        size = len(A)
        self.__size = size

        length = 2 * pow(2, math.floor(math.log(size) / math.log(2)) + 1)
        self.__tree = [0 for i in range(length)]

        self.build()

    def build(self, b=0, e=-1, node=1):

        A = self.__A
        code = self.__code
        size = self.__size

        if e == -1:
            e = size - 1

        if b == e:
            if code == 0:
                self.__tree[node] = A[b]
            else:
                self.__tree[node] = b
        else:
            leftIndex = 2*node
            rightIndex = 2*node + 1

            self.build(b, (b+e)//2, leftIndex)
            self.build((b+e)//2 + 1, e, rightIndex)

            leftContent = self.__tree[leftIndex]
            rightContent = self.__tree[rightIndex]

            if code == 0:
                self.__tree[node] = leftContent + rightContent
            else:
                leftValue = A[leftContent]
                rightValue = A[rightContent]

                if code == 1:
                    if leftValue <= rightValue:
                        self.__tree[node] = leftContent
                    else:
                        self.__tree[node] = rightContent

                else:
                    if leftValue >= rightValue:
                        self.__tree[node] = leftContent
                    else:
                        self.__tree[node] = rightContent

    def query(self, i, j, b=0, e=-1, node=1):

        code = self.__code
        A = self.__A

        if e == -1:
            e = self.__size - 1
        
        if i > e or j < b:
            return -1

        if b >= i and e <= j:
            return self.__tree[node]

        p1 = self.query(i, j, b, (b+e)//2, 2*node)
        p2 = self.query(i, j, (b+e)//2 + 1, e, 2*node + 1)

        if p1 == -1:
            return p2
        if p2 == -1:
            return p1

        if code == 0:
            return p1 + p2
        elif code == 1:
            if A[p1] <= A[p2]:
                return p1
            else:
                return p2
        else:
            if A[p1] >= A[p2]:
                return p1
            else:
                return p2


if __name__ == "__main__":

    A = [8, 7, 3, 9, 5, 1, 10]

    tree = SegmentTree(A, 1)

    assert tree.query(3, 3) == 3
    assert tree.query(1, 3) == 2
    assert tree.query(0, 6) == 5
    assert tree.query(4, 6) == 5

    tree = SegmentTree(A, 2)

    assert tree.query(4, 4) == 4
    assert tree.query(0, 6) == 6
    assert tree.query(2, 4) == 3
    assert tree.query(1, 2) == 1

    tree = SegmentTree(A,  0)

    assert tree.query(0, 0) == 8
    assert tree.query(0, 6) == 43
    assert tree.query(1, 2) == 10
    assert tree.query(1, 3) == 19
    assert tree.query(4, 5) == 6

    print("Segment tree python done")
