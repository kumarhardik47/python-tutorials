import os
import threading
from threading import Thread
class Sample(Thread):
	def __init__(self):
		pass

	@classmethod
	def run(self):
		print "sample run"


for i in range(10):
	#threading.thread.start(target=Sample.run())
	t = Thread.start(target=Sample.run())
	t.join()


