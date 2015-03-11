'''
    type: algorithm
    theme: arrays
    sub-theme: sorting
    name: insertion sorting
    author of code: Evgeny @missingdays Bovykin

'''

def insertionSort(ar):

    for i in range(1, len(ar)):

        #Get new element
        current_value = ar[i]
        #Get position of this element
        position = i

        #While new element is bigger than compared value
        while(position > 0 and ar[position-1] > current_value):

            #Dive this element down
            ar[position] = ar[position-1]
            position = position - 1

        #Write element to its new place
        ar[position] = current_value

#Array we will sort
ar = [0, 1, 10, 15, 7, 20, 4, 6, 90, 5]

#Sort it
insertionSort(ar)

#Print it
for i in range(len(ar)):
    print(ar[i])
