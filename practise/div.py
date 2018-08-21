import os
import time
def main():
	nums = []
	for num in range(2000, 3200 ):
		if num%7 is 0 and not num%5 is 0:
			nums.append(num)
	print nums
if __name__ == "__main__":
	main()
