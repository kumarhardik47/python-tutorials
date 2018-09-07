import os

class Fib:
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def next(self):
		retval = self.a +self.b
		self.a = self.b
		self.b = retval
	
		return retval

fib = iter(Fib())
print 0
print 1
for i in range(10):
	print next(fib)

		
