import os

class A:
	def __init__(self):
		print 'A' * 80
		#pass

	def message(self):
		print 'A' * 80
		print "Sending message from A"
class B(A,object):
	def __init__(self):
		print 'B' * 80
		super(B,self).__init__()
		print "B constructor"
		#pass

	def message(self):
		print 'B' * 80
	 	super(B,self).message()	
		print "Sending message from B"
class C(B,A,object):
	def __init__(self):
		print 'C' * 80
		super(C,self).__init__()
		print "C constructor"
	#	pass

	def message(self):
		print 'C' * 80
	 	super(C,self).message()	
		print "Sending message from c"
	#pass



c = C()

c.message()
