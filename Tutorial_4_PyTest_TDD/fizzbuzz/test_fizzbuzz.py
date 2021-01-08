from fizz import buzz
from checker import has_3
from checker import has_5

def test_fizzbuzz():
	# we should be able to print numbers up to 100, wich is 5*20
	assert buzz(100)=="Buzz"
def test_3():
	# if a number is 3 we should print Bizz
	assert buzz(3)=="Fizz"
def test_5():
	# if a number is 5 we should print Buzz
	assert buzz(5)=="Buzz"
def test_0():
	# we should start counting on 1
	assert buzz(0)==False
#Checker tests
def test_ch3():
	assert has_3(384)
def test_ch3_2():
	assert has_3(222)==False
def test_ch5():
	assert has_5(543)
def test_ch5_2():
	assert has_5(222)==False
