#Get number of testcases
n = int(input().split()[1])

#Get service lane
road = list(map(int, input().split()))

#For every test case
for i in range(n):

    #Assume all three cars can pass through
    car = 3

    #Get test case
    #[0] = beginning
    #[1] = end
    case = list(map(int, input().split()))

    #Go through the path we have to pass through
    for k in range(case[0], case[1] + 1):

        #If road is narrower than current car that can pass
        if road[k] < car:

            #Write that width to current car
            car = road[k]

    #Print what car can go through
    print(car)
