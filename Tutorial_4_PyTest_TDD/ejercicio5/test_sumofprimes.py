from sumas import sum_of_primes

#Si no hay primos debe retornar 0
def test_sum():
	assert sum_of_primes([10,20,30,40]) == 0
def test_other_sum():
	assert sum_of_primes([1,2,3,4,5,6,7])==17
