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
import Gcd

main :: IO()
main = hspec $ do
	describe "Gcd" $ do
		it "returns 1 with 1 0" $ do
			Gcd.gcd 1 0 `shouldBe` 1
		it "returns 1 with 0 1"	$ do
			Gcd.gcd 0 1 `shouldBe` 1
		it "return 1 with 3 5" $ do
			Gcd.gcd 3 5 `shouldBe` 1
		it "return 2 with 4 6" $ do
			Gcd.gcd 4 6 `shouldBe` 2
		it "returns 5 with 10 15" $ do
			Gcd.gcd 10 15 `shouldBe` 5
		it "returns 1 with 17 19" $ do
			Gcd.gcd 17 19 `shouldBe` 1
		it "returns 1 with 18 19" $ do
			Gcd.gcd 18 19 `shouldBe` 1
		it "returns 11 with 99 121" $ do
			Gcd.gcd 99 121 `shouldBe` 11				