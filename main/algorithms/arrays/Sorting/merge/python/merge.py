def mergeSort(Array):

    if len(Array) > 1:

        #Split array in two parts
        mid = len(Array) // 2
        lefthalf = Array[:mid]
        righthalf = Array[mid:]

        #Recursevly sort left and right parts
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #Mergin two sorted arrays
        i = 0 #Left part iterator
        j = 0 #Right part iterator
        k = 0 #Final array iterator

        #While both parts are not empty merge them comparing
        #each element in order
        while i<len(lefthalf) and j<len(righthalf):

            if lefthalf[i] < righthalf[j]:
                Array[k] = lefthalf[i]
                i = i + 1

            else:
                Array[k] = righthalf[j]
                j = j + 1

            k = k + 1

        #There is still something left in the left part. Just copy till the end
        while i < len(lefthalf):
            Array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        #There is still something left in the right part. Just copy till the end
        while j < len(righthalf):
            Array[k]=righthalf[j]
            j=j+1
            k=k+1


Array = [54,26,93,17,77,31,44,55,20]
mergeSort(Array)
print(Array)
