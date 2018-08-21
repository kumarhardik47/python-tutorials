import os
import abc
from abc import ABCMeta, abstractmethod

class sampleAbstract(object):
	__metaclass__ = ABCMeta
	def __init__(self,value):
		super(sampleAbstract,self).__init__()
		self.val = value

	@abstractmethod
	def ret_val(self):
		pass	

class sampleDerived(sampleAbstract):
	def ret_val(self):
		#return self.val*20
		raise NotImplementedError
	#pass

derived = sampleDerived(10)

print derived.ret_val()

