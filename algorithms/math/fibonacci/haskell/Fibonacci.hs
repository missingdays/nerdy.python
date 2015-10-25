#! /usr/bin/env runhugs +l
--
-- fibonacci.hs
-- Copyright (C) 2015 missingdays <missingdays@missingdays>
--
-- Distributed under terms of the MIT license.
--

module Fibonacci where

fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)
