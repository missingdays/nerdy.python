
from .random import Generator

def test_random_sets_seed():
	g = Generator()
	
	g.seed = 0
	assert g.seed == 0

	g.seed = 31415
	assert g.seed = 31415
