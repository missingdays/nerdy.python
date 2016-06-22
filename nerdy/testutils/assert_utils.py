
def assert_sequence_equal(actual, expected):
	"""
	Asserts that two sequences contain the same values
	"""

	assert len(actual) == len(expected)

	for actual_value, expected_value in zip(actual, expected):
		assert actual_value == expected_value