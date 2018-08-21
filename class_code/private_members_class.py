import os

class A:
	a = 1
	_a = 1
	__a = 1

	def __init__(self,a):
		self.a = a

	def print_a(self):
		return self.a
	
	def _print_a(self):
		return self.a
	
	def __print_a(self):
		print self.a

class B(A,object):
	b = 2
	def __init__(self,a):
		super(B,self).__init__(a)
	
	def print_a(self):
		self.a = 25
		return self.a,self._a,self.b
		#print self.__a

	def _print_a(self):
		return self.a,self._a,self.b
	
	def __print_a(self):
		print self.a

a = A(5)
#print "A:__a:",a.__print_a() Private member access outside class
b = B(10)
print "a:",b.print_a()
print "_a:",b._print_a()
print "__a:", b.__print_a()
