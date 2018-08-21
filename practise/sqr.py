import os

def sqr(num):
	d = {}
	for i in range(1,num+1):
		d[i] = i*i;

	return d
if __name__ == "__main__":
	print sqr(8)

