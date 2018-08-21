import os, time
import re

filename = 'sample.txt'
def FileHandler():
	with open(filename,'a+') as fp:
		offset = 0
		while True:
			with open('sample.out','a+') as sample:
				print offset
				fp.seek(offset)
				for i in range(10):
					#if fp.next():
					line = fp.next()
				#for line in lines:
					print line
					out = re.sub("-Technology Systems", "-Hardik Technologies", line)
					sample.write(out)
				sample.close()
				time.sleep(10)
			offset = fp.tell()
				
FileHandler()	
