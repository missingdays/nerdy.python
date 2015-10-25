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
import Factorial

main :: IO ()
main = hspec $ do
    describe "Factorial" $ do
        it "returns 1 from 0" $ do
            fac 0 `shouldBe` 1
        it "returns 1 from 1" $ do
            fac 1 `shouldBe` 1
        it "returns 2 from 2" $ do
            fac 2 `shouldBe` 2
        it "returns 6 from 3" $ do
            fac 3 `shouldBe` 6
        it "returns 24 from 4" $ do
            fac 4 `shouldBe` 24
        it "returns 120 from 5" $ do
            fac 5 `shouldBe` 120

 

