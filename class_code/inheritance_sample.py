



class A(object):
    def go(self):
	print 'A' * 80
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
	print 'B' * 80
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
	print 'C' * 80
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
	print 'D' * 80
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(D,C):
	pass

a = A()
b = B()
c = C()
d = D()
e = E()

#print help(D)
print "A:"
a.go()
print '*' * 80
print "B:"
b.go()
print '*' * 80
print "C:"
c.go()
print '*' * 80
print "D:"
d.go()
print '*' * 80
print "E:"
e.go()
print '*' * 80
