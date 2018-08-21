# 'Hello WORLD" print albhabets that are not in the string "Hello World"

import os
import string

s = "Hello World"

#print ( c for c in s.lower() for i in string.ascii_lowercase)
	
#print filter(lambda x,y: x is not y, x in x.lower()

g = (i for i in string.ascii_lowercase if i not in s.lower())
for g in g:
	print g

#OR#
print [i for i in string.ascii_lowercase if i not in s.lower()]
