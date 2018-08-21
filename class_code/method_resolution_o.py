import os
class A:
    def m(self):
        print("m of A called")

class B(A,object):
    def m(self):
        print("m of B called")
        super(B,self).m()

    def test(self):
	print "Class B test function called"
    
class C(A,object):
    def m(self):
        print("m of C called")
        super(C,self).m()

    def test(self,a):
	print "Class C test function called", a

class D(B,C,object):
    def m(self):
        print("m of D called")
        super(D,self).m()
 
    #def test(self):
	#print "Class C test function called"

d = D()
d.m()
#print help(d)
print '*' * 80
d.test(2)    # This will give error. Because test() in class C overrides the test() from the base class C. Even if you comment the test in class Dit will still give error, because of the super() MRO in C, overrides the test() from B. MRO is the reason for all this. Change the order of class from D(B,C) to D(C,B) and observe.     
print '*' * 80


