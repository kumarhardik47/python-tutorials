import os
class A:
    __a = 0
    _b = 0
    def m(self):
        print("m of A called")

class B(A,object):
    def m(self):
        print("m of B called")
        super(B,self).m()
    
class C(A,object):
    def m(self):
        print("m of C called")
        super(C,self).m()

class D(B,C,object):
    def m(self):
        print("m of D called")
        super(D,self).m()
d = D()
d.m()
print '*' * 80
print d.__a  #this should no such attribute error
print '*' * 80
print A._b
print '*' * 80
#print help(d)
