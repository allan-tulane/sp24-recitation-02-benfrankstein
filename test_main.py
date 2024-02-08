from main import *
from functools import partial
import math


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(10, 4, 3) == 38
	assert simple_work_calc(20, 5, 4) == 70
	assert simple_work_calc(30, 2, 5) == 46

def test_work():
	print(work_calc(10, 2, 2,lambda n: 1))
	print(work_calc(20, 2, 2,lambda n: 1))
	print(work_calc(40, 2, 2,lambda n: 1))
	print(work_calc(60, 2, 2,lambda n: 1))
	print(work_calc(80, 2, 2,lambda n: 1))
	print(work_calc(100, 2, 2,lambda n: 1))

	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(30, 2, 4,lambda n: 1) == 7
	assert work_calc(15, 1, 4,lambda n: 1) == 3
	assert work_calc(30, 3, 2, lambda n: n*n) == 2340
	 
	#lamda n: 1 returns = def f(X): return 1
def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	def work_fn1(n):
		a = 1	
		b = 2
		c = 4
		f = lambda x: x ** c
		return work_calc(n, a, b, f)
	
	def work_fn2(n):
		a = 1
		b = 3
		c = 1
		f = lambda x: x ** c  
		return work_calc(n, a, b, f)

	
	results = compare_work(work_fn1, work_fn2)
	for result in results:
		print(result)


	
	#c = 4 b = 2 a = 2 #greater than
	#c =1 b=2 a=2 #equals
	#c = 0 b = 2 a =2 #less than 
	

	
def test_compare_span():
	def span_fn1(n):
		a = 1	
		b = 2
		c = 4
		f = lambda x: x ** c
		return span_calc(n, a, b, f)
	
	def span_fn2(n):
		a = 1
		b = 3
		c = 1
		f = lambda x: x ** c  
		return span_calc(n, a, b, f)

	
	results = compare_work(span_fn1, span_fn2)
	for result in results:
		print(result)
	#print(span_calc(10, 2, 2,lambda n: 1))
	#print(span_calc(20, 2, 2,lambda n: 1))
	#print(span_calc(40, 2, 2,lambda n: 1))
	#print(span_calc(60, 2, 2,lambda n: 1))
	#print(span_calc(80, 2, 2,lambda n: 1))
	#print(span_calc(100, 2, 2,lambda n: 1))
	pass


if __name__ == "__main__":
	#test_simple_work()
	#test_work()
	#test_compare_work()
	test_compare_span()