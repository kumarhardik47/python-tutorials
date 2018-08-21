import os

def fact(num):
	if (num == 0):
		return 1;
	return num * fact(num-1)

if __name__ == "__main__":
	print fact(8)
