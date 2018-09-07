import os
from threading import Thread

class Sample():
	def __init__(self):
		pass

	@classmethod
	def run(self,i):
		print "sample run:",i


for i in range(10):
	#threading.thread.start(target=Sample.run())
	t = Thread(target=Sample.run(i,))
	t.start()
	t.join()
	print "sample close:" ,i


