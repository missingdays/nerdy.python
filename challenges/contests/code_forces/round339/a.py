#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def calc(l, r, k):

	answ = []

	e = 1

	while e < l:
		e *= k

	if e > r:
		return [-1]

	while e <= r:
		answ.append(e)
		e *= k

	return answ	


l, r, k = [int(i) for i in input().split()]

for elem in calc(l, r, k):
	print(elem, end=" ")

print()	