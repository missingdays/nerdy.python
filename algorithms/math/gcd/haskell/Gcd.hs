#! /usr/bin/env runhugs +l
--
-- Gcd.hs
-- Copyright (C) 2015 missingdays <missingdays@missingdays>
--
-- Distributed under terms of the MIT license.
--

module Gcd where

gcd :: Int -> Int -> Int
gcd a 0 = a
gcd a b = Gcd.gcd b (a`rem`b)