import os

def fib(n,lookup):
	if n == 0 or n ==1:
		lookup[n]=n
	
	if lookup[n] == None:
		lookup[n] = fib(n-1,lookup) + fib(n-2, lookup)

	return lookup[n]


def main():
	n = 10
	lookup = [None] * 200
	print "Fibonacci series for: ", n
	fib(n,lookup)
	for num in lookup:
		if num:
			print num

if __name__ == "__main__":
	main()


