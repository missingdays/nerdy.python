#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

# Number of testcases
n = int(input())

# Map 
m = []

# Init map[n][n]
for i in range(n):
    temp = []
    for k in range(n):
        temp.append(None)
    m.append(temp)

# Function to check whether given cell is cavity
def is_cavity(i, k):
    global m

    c = m[i][k]

    # Check definition
    if c > m[i-1][k] and c > m[i+1][k]:
        if c > m[i][k-1] and c > m[i][k+1]:
            return True
    return False
    

# Read input and save it to map as ints
for i in range(n):

   row = input()
   for k in range(len(row)):
            m[i][k] = int(row[k]) 

# Iterate through map
for i in range(n):
    for k in range(n):

        # If cell is not on the edge
        if  i !=0 and k != 0 and i != n-1 and k != n-1:

            # And it's cavity
            if is_cavity(i, k):
                # Replace it with X
                print("X", end="")
            # Else just print it
            else:
                print(m[i][k], end="")
        else:
            print(m[i][k], end="")
            
    print("")    
