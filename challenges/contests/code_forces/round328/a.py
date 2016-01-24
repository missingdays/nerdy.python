#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

board = []

def check(i, j, fig):
    global board

    if fig == "W":
        while i < 8:
            if board[i][j] == "W":
                return True
            i += 1
    else:
        while i >= 0:
            if board[i][j] == "B":
                return True
            i -= 1
    return False

for i in range(8):
    board.append(input())

bm = 10
wm = 10

for i in range(8):
    for j in range(8):
        if board[i][j] == "B":
            if not check(i+1, j, "W"):
                bm = min(bm, 8 - i)
        elif board[i][j] == "W":
            if not check(i-1, j, "B"):
                wm = min(wm, i + 1)

if wm <= bm:
    print("A")
else:
    print("B")
