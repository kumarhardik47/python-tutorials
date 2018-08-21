#program to check if a given sting has a followed by any number of b

import os
import re

class check_alphanumeric:
	def __init__(self,string):
		self._str = string
		
	def check(self):
		charString = re.compile(r'[ab*]')
		string = charString.search(self._str)
		if string:
			return True
		else:
			return False

if __name__ == "__main__":
	print check_alphanumeric("ajhgdjabgsdjhasjdkqw").check()
	print check_alphanumeric("123wasdsd@##bb").check()


		

