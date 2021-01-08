import pytest

@pytest.mark.parametrize("L",["Hola"])

def test_inverse(L):
	I = "aloH"
	t = inverse(L)
	assert t == I

def inverse(L):
	R = ""
	for i in L:
		R=i+R
	return R
 
