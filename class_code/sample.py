import os

class A:
	def __init__(self):
		print '*' * 80
		self.value = None

	def set_val(self, val):
		self.value = val

	def get_val(self):
		return self.value


class B(A):
	def __init__(self):
		print '#' * 80
		self.value = None

	def set_val(self, val):
		self.value = val

	def get_val(self):
		return self.value

		
if __name__ == "__main__":
	b = B()
	a = A()

	a.set_val(10)
	print a.get_val()

	print b.get_val()

	b.set_val(20)
	print b.get_val()

	
