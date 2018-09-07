import os

file_path = os.getcwd() + "/" +"reverse_file.txt"

def rev_file():
	with open(file_path,"r") as fp:
		lines = fp.readlines()
		for index in range(len(lines)-1, -1, -1):
			print lines[index]
rev_file()

		
