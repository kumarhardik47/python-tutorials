import os


class Employee:
	raise_amt = 1.5
	def __init__(self,fname,lname,salary):
		self.fname = fname
		self.lname = lname
		self.email = fname + lname +"@email.com"
		self.base = salary

	def get_email(self):
		return self.email

	@classmethod
	def change_raise(cls, amt):
		cls.raise_amt = amt
		#return cls.email

	@staticmethod
	def get_fullname():
		return self.fname + self.lname

	@property
	def salary(self):
		#print "salary:", self.salary
		return self.base * self.raise_amt

	@salary.setter
	def salary(self,hike):
		#print "salary:", self.salary
		print "@" * 80
		self.raise_amt = hike

	@salary.deleter
	def salary(self):
		print "@!" * 80
		del self.base


e = Employee("hardik","mahto",75000)
#print e.get_email()
Employee.change_raise(5)
print e.salary
#print e.raise_amt
print "raise:" , e.raise_amt
e.raise_amt = 10
print e.salary, "raise:", e.raise_amt
print "Employee.raise_amt:", Employee.raise_amt
del e.base
del e.fname

#print e.fname
