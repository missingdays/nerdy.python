> Warning: docs are not complete. You can help us adding more information!


#Heapsort
Advance compare-based sorting algorithm
##Idea
Heapsort can be thought of as an improved [selection sort](https://github.com/missingdays/algorithms-library/tree/master/algorithms/arrays/sorting/selection): like that algorithm, it divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.
##Real use
Although somewhat slower in practice on most machines than a well-implemented quicksort, it has the advantage of a more favorable worst-case O(n log n) runtime.

##Performance and complexity
Complexity worst case O(nlogn).

Complexity best case O(n).

Complexity average case O(n).

Memory O(1).

##Visualazition
https://www.cs.usfca.edu/~galles/visualization/HeapSort.html
