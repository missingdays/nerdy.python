/*
 * Copyright (C) 2016
 *
 * Created by missingdays
 * Distributed under terms of the MIT license.
 */
package set

import (
	"sort"
	"testing"
)

func Test_Add(t *testing.T) {
	s := NewSet()

	for i := 0; i < 10; i++ {
		s.Add(i)

		if !s.Has(i) {
			t.Errorf("Set is missing %d", i)
		}
	}
}

func Test_Remove(t *testing.T) {
	s := NewSet()

	for i := 0; i < 10; i++ {
		s.Add(i)

		s.Remove(i)

		if s.Has(i) {
			t.Errorf("Set still has %d", i)
		}

		s.Add(i)

		if !s.Has(i) {
			t.Errorf("Set didn't add %d after deletion ", i)
		}

	}
}

func Test_Keys(t *testing.T) {
	s := NewSet()
	keys := make([]int, 0)

	for i := 0; i < 10; i++ {
		s.Add(i)
		keys = append(keys, i)
	}

	sKeys := s.Keys()

	sort.Ints(sKeys)
	sort.Ints(keys)

	for i := 0; i < 10; i++ {
		if sKeys[i] != keys[i] {
			t.Errorf("Set keys are missing key at %d index", i)
		}
	}
}

func Test_Union(t *testing.T) {
	a := NewSet()
	b := NewSet()

	for i := 0; i < 5; i++ {
		a.Add(i)
		b.Add(i + 5)
	}

	s := Union(a, b)

	for i := 0; i < 10; i++ {
		if !s.Has(i) {
			t.Errorf("Set is missing %d", i)
		}
	}

}
