import os

def num_sum(m, n):
	sums = n
	new_sum = n
	for i in range(m-1):
		len_num =len(str(sums))
		sums= n*(10**len_num )+sums 
		new_sum  = new_sum + sums

	return new_sum



if __name__  == "__main__":

	print num_sum(4,2)
	print num_sum(3,12)


