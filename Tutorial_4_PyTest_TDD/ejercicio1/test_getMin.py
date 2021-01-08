import pytest

@pytest.mark.parametrize("values",[[1,5,324,6,2,3,3],[2,6,3,12,523,754,1],[3,546,6,23,52,35,564,756,2,1]])

def test_min(values):
	min  = get_min(values)
	assert min == 1
def get_min(values):
	k = 4
	for i in values:
		if i<k:
			k=i
	return k
	
