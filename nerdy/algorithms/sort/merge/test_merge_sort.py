
from nerdy.algorithms.array import shuffle, equal

from . import merge_sort

def test_merge_sort():

	n = 100

	assert equal(merge_sort([]), [])
	assert equal(merge_sort([1]), [1])
	assert equal(merge_sort([1, 2]), [1, 2])
	assert equal(merge_sort([1, 2, 3]), [1, 2, 3])
	assert equal(merge_sort(list(range(n))), list(range(n)))

	assert equal(merge_sort([2, 1]), [1, 2])
	assert equal(merge_sort([3, 2, 1]), [1, 2, 3])
	assert equal(merge_sort([3, 1, 2]), [1, 2, 3])
	assert equal(merge_sort([2, 1, 3]), [1, 2, 3])
	assert equal(merge_sort([2, 3, 1]), [1, 2, 3])
	assert equal(merge_sort([1, 3, 2]), [1, 2, 3])

	assert equal(merge_sort([1, 1, 1, 1,]), [1, 1, 1, 1])
	assert equal(merge_sort([1, 2, 2, 2, 3]), [1, 2, 2, 2, 3])
	assert equal(merge_sort([3, 2, 2, 2, 1]), [1, 2, 2, 2, 3])
	assert equal(merge_sort([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
	assert equal(merge_sort([3, 3, 2, 2, 1, 1]), [1, 1, 2, 2, 3, 3])

	for i in range(n):
		l = shuffle(list(range(n)))

		assert equal(merge_sort(l), list(range(n)))
