import os

class rectangle:
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length * self.breadth 

	def __add__(rectangle1,rectangle2):
		l = rectangle1.length +rectangle2.length
		b = rectangle1.breadth +rectangle2.breadth
		r = rectangle(l,b)
		return r

rect1 = rectangle(3,5)
print "rect1 Area:", rect1.area()
 
rect2 = rectangle(4,5)
print "rect2 Area:", rect2.area()

r = rect1 + rect2
print "R area: ",r.area()
	
