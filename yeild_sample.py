import os


def gen_square(num):
	#if num<0:
	#	return -1

	for i in range(num):
		#print i**2  #uncomment and see behaviour
		yield i**2

if __name__ == "__main__":
	#print gen_square(-5)
	#print gen_square(0)
	for i in gen_square(5):
		print i



