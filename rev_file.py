import os
from itertools import islice



#islice(iterable, start,stop,step)
f = os.getcwd() + "/" + "reverse_file.txt"
with open(f,'r') as fp:
	for line in islice(fp, 2):
		#print only two lines
		print line
		



	#s = islice(fp, 0,2 -1
	#s = fp.readlines()
	#print s
	#print s[::-1]
