######### Iterator example
# Must implement __iter__() and next().
import os

class Counter:          #receives two numbers and creates an iterator for the range in between the numbers
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self): # return the iterator object.
		return self

	def next(self):
		if self.current > self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.current - 1


for i in Counter(5,10):
	print i
