import os
import json

f = os.getcwd() + "/" + "sample.txt"

with open(f,'r') as fp:
	data = json.dumps(json.loads(fp.read()))
	print data, type(data) 
	
