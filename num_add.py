import os

#      2
#    2 2
#  2 2 2
#2 2 2 2
#-------
#2 4 6 8
def num_sum(m, n):
	for i in range(m):	
		i+= 1
		a = str(n)*i
		yield a

if __name__  == "__main__":

	gen1 = num_sum(4,2)
	sums = 0
	for g in gen1:
		num1 += int(g)
		sums += num1
	print sums


