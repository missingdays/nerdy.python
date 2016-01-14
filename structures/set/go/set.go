/*
 * Copyright (C) 2016
 *
 * Created by missingdays
 * Distributed under terms of the MIT license.
 */

package set

type Set struct {
	keys map[int]struct{}
}

func NewSet() *Set {
	set := Set{}
	set.keys = make(map[int]struct{})
	return &set
}

func Union(a *Set, b *Set) *Set {
	s := NewSet()

	keys := a.Keys()

	for _, key := range keys {
		s.Add(key)
	}

	keys = b.Keys()

	for _, key := range keys {
		s.Add(key)
	}

	return s
}

func (s *Set) Add(value int) {
	s.keys[value] = struct{}{}
}

func (s *Set) Has(value int) bool {
	_, has := s.keys[value]
	return has
}

func (s *Set) Remove(value int) {
	delete(s.keys, value)
}

func (s *Set) Keys() []int {

	keys := make([]int, 0, len(s.keys))

	for k := range s.keys {
		keys = append(keys, k)
	}

	return keys
}
