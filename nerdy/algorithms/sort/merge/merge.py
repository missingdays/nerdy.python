def merge_sort(array):
    """
    Sorts input array using merge sort algorithm
    Returns new array. For algorithms sorting in place see nerdy.algorithm.sort_in_place

    Average and worst time:
    O(n logn)

    Space:
    O(n logn)
    """

    if len(array) < 2:
        return array

    #Split array in two parts
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    #Recursevly sort left and right parts
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    """
    Returns new sorted array consisting of left and right value
    Left and right arrays should be sorted
    """

    i = 0 #Left part iterator
    j = 0 #Right part iterator
    
    array = []

    #While both parts are not empty merge them comparing
    #each element in order
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i = i + 1
        else:
            array.append(right[j])
            j = j + 1

    #There is still something left in the left part
    while i < len(left):
        array.append(left[i])
        i = i + 1

    #There is still something left in the right part
    while j < len(right):
        array.append(right[j])
        j=j+1

    return array