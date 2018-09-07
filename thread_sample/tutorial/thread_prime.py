import os
import threading
from threading import Thread

class PrimeNumber(threading.Thread):
	def __init__(self,number):
		threading.Thread.__init__(self)
		self.number = number


	def run(self):
		counter = 2
		is_prime = True
		while counter < self.number:
			if self.number % counter == 0:
				print "%s is not prime number" % (self.number)
				is_prime = False
				return
			counter += 1
		if is_prime:
			print "%s is prime number" % (self.number)

threads = []
while(True):
	number = int(raw_input("Enter the number:"))
	if number <1:
		break

	thread = PrimeNumber(number)
	thread.start()
	threads += [thread]
	print threads, type(thread)

	for thread in threads:
		thread.join()
	



