import math

def is_prime(num):
	#Prime numbers must be greater than 1
	if num<2:
		return False
	#We only need to check dividers that are lower than the sqrt of our prime
	for n in range(2, math.floor(math.sqrt(num)+1)):
		if num % n == 0:
			return False
	return True
