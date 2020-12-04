from checker import has_3
from checker import has_5
def buzz(n):
	a=False
	for i in range (1,n+1):
		a=""
		if i%3==0 or has_3(i):
			a+="Fizz"
		if i%5==0 or has_5(i):
			a+="Buzz"
		if a=="":
			a=i
		print(a)
	return a
buzz(150)
