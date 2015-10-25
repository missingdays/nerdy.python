#! /usr/bin/env runhugs +l
--
-- spec.hs
-- Copyright (C) 2015 missingdays <missingdays@missingdays>
--
-- Distributed under terms of the MIT license.
--

import Test.Hspec
import Test.QuickCheck
import Control.Exception (evaluate)
import Fibonacci

main :: IO ()
main = hspec $ do
    describe "Fibonacci" $ do
        it "returns 0 as 0 element" $ do
            fib 0 `shouldBe` 0
        it "returns 1 as 1 element" $ do
            fib 1 `shouldBe` 1
        it "2 is 2" $ do
            fib 2 `shouldBe` 1
        it "3 is 3" $ do
            fib 3 `shouldBe` 2
        it "4 is 5" $ do
            fib 4 `shouldBe` 3
        it "5 is 8" $ do 
            fib 5 `shouldBe` 5
        it "6 is 13" $ do
            fib 6 `shouldBe` 8
        it "7 is 21" $ do
            fib 7 `shouldBe` 13





