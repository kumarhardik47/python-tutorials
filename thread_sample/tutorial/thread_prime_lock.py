import os
import threading

class PrimeNumber(threading.Thread):
	prime_numbers = {}
	lock = threading.Lock()
	def __init__(self,number):
		threading.Thread.__init__(self)
		self.number = number
		PrimeNumber.lock.acquire()
		PrimeNumber.prime_numbers[number] = "None"
		PrimeNumber.lock.release()
		

	def run(self):
		counter = 2
		is_prime = True
		while counter < self.number:
			if self.number % counter == 0:
				is_prime = False
			counter += 1
		PrimeNumber.lock.acquire()
		PrimeNumber.prime_numbers[self.number] = is_prime
		PrimeNumber.lock.release()
		print PrimeNumber.prime_numbers

threads = []
while(True):
	number = int(raw_input("Enter the number:"))
	if number <1:
		break

	thread = PrimeNumber(number)
	thread.start()
	threads += [thread]
	#print threads, type(thread)

	for thread in threads:
		thread.join()
	



