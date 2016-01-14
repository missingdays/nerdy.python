/*
 * Copyright (C) 2016
 *
 * Created by missingdays
 * Distributed under terms of the MIT license.
 */
package factorization

import (
	"sort"
	"testing"
)

func Test_PrimeFactors(t *testing.T) {

	test([]int{2, 3}, 6, t)
	test([]int{2, 2}, 4, t)
	test([]int{2, 2, 2}, 8, t)
	test([]int{2, 3, 5, 7}, 210, t)
	test([]int{2, 5, 7}, 70, t)
	test([]int{11, 13}, 143, t)
	test([]int{31, 31}, 961, t)
	test([]int{523}, 523, t)
	test([]int{523, 523, 523, 523}, 74818113841, t)

}

func test(factors []int, number int, t *testing.T) {

	actual := PrimeFactors(number)

	sort.Ints(factors)
	sort.Ints(actual)

	if !equal(factors, actual) {
		t.Errorf("Expected %v but found %v", factors, actual)
	}
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}
