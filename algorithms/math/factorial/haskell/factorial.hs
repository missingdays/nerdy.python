#! /usr/bin/env runhugs +l
--
-- factorial.hs
-- Copyright (C) 2015 missingdays <missingdays@missingdays>
--
-- Distributed under terms of the MIT license.
--

fac 0 = 1
fac n = fac(n-1) * n

main = print(fac 10)
