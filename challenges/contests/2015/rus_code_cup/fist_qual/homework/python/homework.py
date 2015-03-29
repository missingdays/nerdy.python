
#For every test case
for i in range(int(input())):

    #Get those numbers
    x = int(input())
    y = int(input())
    z = int(input())

    #If they are equal in 10 notation
    #they are equal and in bigger notations
    if x * y == z:
        print('Infinity')
        
    #If they are not equal in 10 notation
    #they are not equal and in bigger notations
    #and that means there are only finite number
    #of notations
    else:
        print('Finite')
