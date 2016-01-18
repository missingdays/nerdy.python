#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

import math

def pythagoras(p, p1):
	return math.sqrt(pow(p[0]-p1[0], 2) + pow(p[1]-p1[1], 2))

def distance(p, p1, p2):

	# Some mad math here.
	# Basicly we are calculating distance between point p and line between p1 and p2
	
	# Line is horizontal
	if p2[1] == p1[1]:
		if p[0] < min(p1[0], p2[0]) or p[0] > max(p1[0], p2[0]):
			return pythagoras(p, p1)
		else:
			return abs(p1[1] - p[1])

	# Line is vertical
	if p2[0] == p1[0]:
		if p[1] < min(p1[1], p2[1]) or p[1] > max(p1[1], p2[1]):
			return pythagoras(p, p1)
		else:
			return abs(p1[0] - p[0])

	k = (p2[1] - p1[1]) / (p2[0] - p1[0])
	b = p2[1] - k*p2[0]

	k0 = -1/k
	b0 = p[1] - k0*p[0]

	x = (b-b0) / (k0 - k)
	y = k*x + b

	if x < min(p1[0], p2[0]) or x > max(p1[0], p2[0]):
		return pythagoras(p, p1)
	else:
		return math.sqrt(pow(p[0]-x, 2) + pow(p[1]-y, 2))



def calc(v, p):
	m = float("inf")

	for i in range(len(v)-1):
		m = min(m, distance(p, v[i], v[i+1]))

	m = min(m, distance(p, v[0], v[len(v)-1]))
	
	return m

n, x, y = [int(i) for i in input().split()]
v = []

sr = 0
br = 0

for i in range(n):
	a, b = [int(k) for k in input().split()]

	v.append([a, b])

	r = math.sqrt(pow(a-x, 2) + pow(b-y	, 2))

	br = max(br, r)

sr = calc(v, [x, y])

print(math.pi * (pow(br, 2) - pow(sr, 2)))	