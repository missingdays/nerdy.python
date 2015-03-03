A = [7, 8, 9, 15, 20, 34, 41, 45] #Sorted array required

def binarySearch(array, item):
    first = 0
    last = len(array)-1
    found = False

    while first <= last and not found:

        midpoint = (first + last) // 2

        if array[midpoint] == item:
            found = True

        else:
            if item < array[midpoint]:
                last = midpoint - 1

            else:
                first = midpoint + 1
    return found


print(binarySearch(A, 3)) #Not found
print(binarySearch(A, 45)) #Found
