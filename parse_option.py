import os
import optparse

#nothing should be in between args and kwargs
def pars(e,f,*args,**kwargs):
	print e,f
	print type(args), type(kwargs)
	print '*' * 80
	for k in kwargs:
		print kwargs[k]

#if __name__ == "__main__":
#	main(1,2,2, 4,a="6",g="4")

pars(1,2,3,4,5,6,2,0,3,a=6,b=7)
