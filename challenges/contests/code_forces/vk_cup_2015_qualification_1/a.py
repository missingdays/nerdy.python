#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())

def DFS(node, name, found):
    if node.name == name:
        return node
    found.add(node)
    for child in node.childs:
        if not child in found:
            n = DFS(child, name, found)
            if n != None:
                return n
    return None

class Node():
    def __init__(self, name):
        self.name = name
        self.childs = []

class Tree():
    def __init__(self, root):
        self.root = root

    def add(self, name, to):
        found = set()
        node = DFS(self.root, to, found)
        node.childs.append(Node(name))

    def max_depth(self, node):
        m = 1
        for child in node.childs:
            n = 1 + self.max_depth(child)
            if n > m:
                m = n 
        return m


tree = Tree(Node("polycarp"))

for i in range(n):
    inp = input().lower().split()

    tree.add(inp[0], inp[2])

print(tree.max_depth(tree.root))    
