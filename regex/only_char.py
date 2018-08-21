#program to check if a given sting has only A-Za-z0-9

import os
import re

class check_alphanumeric:
	def __init__(self,string):
		self._str = string
		
	def check(self):
		pattern = re.compile(r'[^A-Za-z0-9]')
		string = pattern.search(self._str)
		return not bool(string)

if __name__ == "__main__":
	print check_alphanumeric("ajhgdjagsdjhasjdkqw").check()
	print check_alphanumeric("123wasdsd@##").check()


		

