#Get number of test cases
n = int(input())

for i in range(n):
    #Initial height
    h = 1
    #Number of cycles
    c = int(input())

    #Multiply by 2 or add 1
    #depending on what cycle it is
    for k in range(c):
        #Even cycle
        if(k % 2 == 0):
            h = h * 2
        #Odd cycle
        else:
            h = h + 1
            
    print(h)
