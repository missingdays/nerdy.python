#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_list_list(n):
    return [[] for i in range(n)]

dp = new_list(100001)
g = new_list_list(100001)

n, m = read_list()

for i in range(m):
    v, u = read_list()

    g[v].append(u)
    g[u].append(v)

answ = 0

for v in range(1, n+1):
    dp[v] = 1

    for u in g[v]:
        if u < v:
            dp[v] = max(dp[v], dp[u]+1)

    answ = max(answ, dp[v]*len(g[v]))

print(answ)
