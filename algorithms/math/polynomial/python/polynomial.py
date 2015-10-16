
def calc(pol, x):
	result = pol[0]
	for i in range(1, len(pol)):
		result *= x
		result += pol[i]
	return result
	

if __name__ == "__main__":
	assert calc([1, 2, 3], 1) == 6
	assert calc([1, 2, 3], 2) == 11
	assert calc([3, 2, 1], 1) == 6
	assert calc([3, 2, 1], 2) == 17
	print("Polynomial python done")