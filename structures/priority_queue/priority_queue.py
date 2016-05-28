#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

class PriorityQueue():
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        self.siftUp(len(self.values)-1)

    def getMax(self):
        value = self.values[0]
        if len(self.values) == 1:
            self.values.pop()
            return value
        self.values[0] = self.values.pop()

        self.siftDown(0)

        return value

    def swap(self, i1, i2):
        self.values[i1], self.values[i2] = self.values[i2], self.values[i1]

    def siftUp(self, i):
        while i > 0 and self.values[i] > self.values[i//2]:
            self.swap(i, i//2)
            i //= 2

    def siftDown(self, i):
        l = len(self.values)
        while i*2 < l:
            left = i*2
            right = i*2+1
            j = left
            if right < l and self.values[right] > self.values[left]:
                j = right
            if self.values[i] >= self.values[j]:
                return
            self.swap(i, j)
            i = j
                

if __name__ == "__main__":
    h = PriorityQueue()

    h.insert(5)
    h.insert(10)

    assert h.getMax() == 10
    assert h.getMax() == 5

    h.insert(5)
    h.insert(10)
    h.insert(7)
    
    assert h.getMax() == 10

    h.insert(6)

    assert h.getMax() == 7
    assert h.getMax() == 6

    h.insert(1)
    h.insert(2)
    h.insert(3)
    h.insert(4)
    h.insert(5)

    assert h.getMax() == 5
    assert h.getMax() == 5
    assert h.getMax() == 4
    assert h.getMax() == 3
    assert h.getMax() == 2
    assert h.getMax() == 1

    print("Priority queue python done")
