#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_lowercase

# Gets girl index
def get_girl(c):
    return ascii_lowercase.index(c)

# Checks if all boys found their girls
def perfect(pool):
    for elem in pool:
        if len(elem) != 1:
            return False
    return True    

# Find the best boy in current pool considering girls preferences 
def find_best(girl, current_boys):
    for prefer in girl:
        for boy in current_boys:
            if prefer == boy:
                return boy

def clear(N):
    return [[] for i in range(N)]

N = 5 # number of boys and girls

# Boys' preferences 
# e.x. boys[0] like 'c' the most, then 'b' and so on
boys = [
         [ "c", "b", "e", "a", "d" ],
         [ "a", "b", "e", "c", "d" ],
         [ "d", "c", "b", "a", "e" ],
         [ "a", "c", "d", "b", "e" ],
         [ "a", "b", "d", "e", "c" ]
       ]

# Girl's preferences
girls = [
         [ 2, 4, 1, 0, 4 ],
         [ 4, 1, 0, 3, 2 ],
         [ 3, 2, 4, 0, 2 ],
         [ 0, 1, 2, 3, 4 ],
         [ 1, 2, 3, 0, 4 ]
        ]

# Boys who "propose" to each girl
boys_pool = [[] for i in range(N)]

while not perfect(boys_pool):

    # Boys "propose" to their best girl
    # who hasn't rejected him yet
    for i in range(N):
        boys_pool[get_girl(boys[i][0])].append(i) # boys choose the best girl

    for i in range(N):
        current_boys = boys_pool[i]
        
        # Girl finds the best boy who "proposed" to her
        current_best = find_best(girls[i], current_boys)

        # And rejects others
        for boy in boys_pool[i]:
            if boy != current_best:
                boys[boy].pop(0) 

    if not perfect(boys_pool):
        boys_pool = clear(N)

print(boys_pool)                
