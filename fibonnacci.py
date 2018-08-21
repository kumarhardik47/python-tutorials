import os

a = 0
b = 1

'''
def fib(num):
	global a,b
	print a
	print b
	for i in range(num-2):
		c = a+b
		a = b
		b = c
		#print "a:",a,    "b:",b, "c:",c
		print c
		
fib(10)

'''

###############OR##########################

'''
def fib(num):
	a = 0
	b=1
	print a
	print b
	for i in range(num-2):
		c = a+b
		a = b
		b = c
		print c
fib(10)
'''

###########################using yield##################

def fib():
	a,b = 0,1
	while 1:          #infinite generator
		yield a
		a,b = b,a+b

itr = fib()
for i in range(10):  #infiniteness limited using range(10) upto 10.
	print itr.next()

