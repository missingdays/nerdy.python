/*
 * Copyright (C) 2016
 *
 * Created by missingdays
 * Distributed under terms of the MIT license.
 */
package factorization

func PrimeFactors(n int) []int {
	i := 2
	factors := make([]int, 0)

	for i*i <= n {
		if n%i == 0 {
			factors = append(factors, i)

			n /= i
		} else {
			i += 1
		}
	}

	if n > 1 {
		factors = append(factors, n)
	}

	return factors

}
