import os
import re

n1 = "4253625879615786"
n2 = "4424424434424444"
n3 = "5122-2368-7954-3214"

#pattern = re.compile('^(4,5,6)[0-9]{3}\1+(-)?')
pattern = re.compile(r'(?!.*(\d)(-?\1){3})')
out = re.search(pattern,n1)
if out:
	for o in out:
		print o

