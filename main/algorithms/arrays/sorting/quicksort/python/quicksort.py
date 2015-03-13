'''
    type: algorithm
    theme: arrays
    sub-theme: sorting
    name: quick sorting
    author of code: Evgeny @missingdays Bovykin

'''

#Sort array using quicksort algorithm
def quickSort(arr):

    #Array that is less than pivot
    less = []

    #List of numbers that are equal to pivot
    pivotList = []

    #Array that is greated than pivot
    greater = []

    #If array contains only one number it doesn't need to be sorted
    if len(arr) <= 1:

        #So return it
        return arr
    #If array is greater though
    else:

        #Choose pivot - the number that we will compare all other numbers to
        pivot = arr[0]

        #Now compare it
        for i in arr:

            #If number is less than pivot
            if i < pivot:

                #Append it to less array
                less.append(i)

            #If number is greater than pivot
            elif i > pivot:

                #Append it to greater array
                greater.append(i)
            #If number equals to pivot
            else:

                #Append it to list of pivots
                pivotList.append(i)

        #Sort left part
        less = quickSort(less)

        #Sort right part
        greater = quickSort(greater)

        #Concatenate in sorted order and return
        return less + pivotList + greater

#Array to be sorted
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print(a)
print('unsorted')

#Sort it!
a = quickSort(a)
print(a)
print('sorted')
