import pytest

@pytest.mark.parametrize("n",[4,5,6])

def test_fibonacci(n):
	conocidos=[0,1,1,2,3,5,8,13,21,34,55,89]
	res = conocidos[n]
	assert fibonacci(n) == res

def fibonacci(n):
	if n == 0:
		return 0
	elif n==1:
		return 1
	else:
		return(fibonacci(n-1)+fibonacci(n-2))
