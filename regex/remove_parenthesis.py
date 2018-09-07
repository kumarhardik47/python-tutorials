import os
import re

s = "[\"example (.com)\", \"w3resource\", \"github (.com)\", \"stackoverflow (.com)\"]"

out = re.split('\[|\"|\(|\)|\.|,|\]| ',s)
i = []
for o in out:
	if o: 
		i.append(o)

print i
