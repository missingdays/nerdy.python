#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_lowercase

def indx(c):
    global ascii_lowercase

    return ascii_lowercase.index(c)

def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]

n, m = read_list()
n += 1

string = new_list(n)

v = new_matrix(n, n)

for i in range(m):
    v1, v2 = read_list()

    v[v1][v2] = True
    v[v2][v1] = True

for i in range(1, n):
    l = v[i].count(True)

    if l == n-2:
        string[i] = 'b'

for i in range(1, n):
    if string[i]:
        continue
    string[i] = 'a'

    for j in range(1, n):
        if string[j]:
            continue
        if v[i][j] == True:
            string[i] = 'a'
        else:
            string[i] = 'c'

for i in range(1, n):
    for j in range(1, n):
        if i == j:
            continue
        if (abs(indx(string[i])-indx(string[j])) == 2 and v[i][j]) or (abs(indx(string[i])-indx(string[j])) < 2 and not v[i][j]):
            print("No")
            exit()
print("Yes")
for i in range(1, n):
    print(string[i], end="")
print()
