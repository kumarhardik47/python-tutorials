import os

def reverse_string(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]
		
if __name__ == "__main__":
	s = "Hello World"
	reversed_string = ""
	iterator = reverse_string(s)
	for i in iterator:
		reversed_string += i

	print (reversed_string)
