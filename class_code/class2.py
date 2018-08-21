class Foo(object):
    a = 0
    _a = 1
    __a = 2
    b = 3
    def __init__(self):
	    self.a = 1

    def bar(*args):
        print args


    @classmethod
    def baaz(*args):
        print args

    @staticmethod
    def quux(*args):
        print args
	print self.a            ######## self is not allowed in static method. So this will give error
	print b			########Will cause error because of staticmethod 
	print self._a, elf.__a  ######  Will cause error because of staticmethod

class FooDerived(Foo):

	def __init__(self):
		pass

	def single_score(self):
		print self._a


	def double_score(self):
		self.__a = 20
		print self.__a

foo_derive = FooDerived()
foo_derive.single_score()
foo_derive.double_score()
print '*' * 80

foo = Foo()
print "hasattr:", hasattr(foo,"a") #True
print "hasattr:", hasattr(foo,"_a") #True
print "hasattr:", hasattr(foo,"__a") #False
print foo._a
print foo.__a
#Foo.bar(123)
#print dir(Foo)
Foo.baaz(1,2,3)
Foo.quux(1,2,3)
print '*' * 80
foo.bar(1,2,3)
foo.baaz(1,2,3)
foo.quux(1,2,3)
print '*' * 80

