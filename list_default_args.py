import os

def list_args(val, l=[]):
	l.append(val)
	return l

a1 = list_args(10)
print a1
a2 = list_args(20,[])
print a2
a3 = list_args(30)
print a3
######################################################################################################################################
#   Once we define the function, it creates a new list. Then, whenever we call it again without a list argument,                     #
#   it uses the same list. This is because it calculates the expressions in the default arguments when we define the function,       #
#   not when we call it.                                                                                                             #
######################################################################################################################################
