> Warning: docs are not complete. You can help us adding more information!


#Binary search
Algorithm that finds the specific value in sorted array.
##Idea
For binary search, the array should be arranged in ascending or descending order. In each step, the algorithm compares the search key value with the key value of the middle element of the array. If the keys match, then a matching element has been found and its index, or position, is returned. Otherwise, if the search key is less than the middle element's key, then the algorithm repeats its action on the sub-array to the left of the middle element or, if the search key is greater, on the sub-array to the right. If the remaining array to be searched is empty, then the key cannot be found in the array and a special "not found" indication is returned.
##Real use
Used as the best search algorithm.

##Performance and complexity
Worst case performance O(logn).

Best case performance O(1).

Memory O(1).

##Visualazition
http://www.dave-reed.com/book/Chapter8/search.html
