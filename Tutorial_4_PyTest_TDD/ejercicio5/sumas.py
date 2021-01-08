from primes import is_prime

def sum_of_primes(L):
	R=0
	for i in L:
		if (is_prime(i)):
			R+=i
	return R
