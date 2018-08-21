import os

class Fib:
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def next(self):
		retval = self.a
		self.a = self.b
		self.b = self.a + self.b
	
		return retval

fib = iter(Fib())
for i in range(3):
	print next(fib)

		
