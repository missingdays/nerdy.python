
#Get number of jars and number of operations
n = raw_input().split()

#Convert them to integers
n = map(int, n)

#Sum of all additions
sum = 0

#For every operation
for i in range(n[1]):

    #Get first jar, last jar and number of candies to be added
    raw = raw_input().split()

    #Convert them to integers
    raw = map(int, raw)

    #Add total number of candies to sum
    #sum += (last jar - first jar + 1) * number of candies
    sum += (raw[1] - raw[0] + 1) * raw[2]

#Print average number of candied
print sum / n[0] # Sum / number of jars
