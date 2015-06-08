#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Solution for python lists chalenge
"""

arr = []

for i in range(int(input())):
    inp = input().split()

    if inp[0] == "append":
        arr.append(int(inp[1]))
    elif inp[0] == "extend":
        arr.extend(int(inp[1]))
    elif inp[0] == "insert":
        arr.insert(int(inp[1]), int(inp[2]))
    elif inp[0] == "remove":
        arr.remove(int(inp[1]))
    elif inp[0] == "pop":
        arr.pop()
    elif inp[0] == "index":
        arr.index(int(inp[1]))
    elif inp[0] == "count":
        arr.count(int(inp[1]))
    elif inp[0] == "sort":
        arr.sort()
    elif inp[0] == "print":
        print(arr)
    else:
        arr.reverse()
   
