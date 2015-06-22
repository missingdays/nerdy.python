#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

# For every test case
for i in range(int(input())):
    
    # Get colors
    BW = list(map(int, input().split()))

    # Get prices
    XYZ = list(map(int, input().split()))
    
    # If converting is better
    if XYZ[0] > XYZ[1] + XYZ[2]:
    
        # Always convert 
        XYZ[0] = XYZ[1] + XYZ[2]

    elif XYZ[1] > XYZ[0] + XYZ[2]:

        XYZ[1] = XYZ[0] + XYZ[2]

    # Print the whole price
    print(BW[0]*XYZ[0] + BW[1]*XYZ[1])
