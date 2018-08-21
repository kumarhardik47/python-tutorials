import os
import re

email = raw_input("Please enter email-id:\n")

pattern = re.compile('[a-zA-Z0-9]{3,49}@[a-zA-Z]{3,15}.com')
out = re.search(pattern,email)
if out:
	print "Valid"
else:
	print "no valid email id"


