import os

class A:  
    def __init__(self):  
        self.name = 'John'  
        self.age = 23  
  
    def getName(self):  
        return self.name  
  
  
class B:  
    def __init__(self):  
        super(B,self).__init__()  
        self.name = 'Richard'  
        self.id = '32'  
  
    def getName(self):  
        return self.name  
  
  
class C(A, B,object):  
    def __init__(self):  
        super(C,self).__init__()
	######OR###########iand observe the behavior of super. it ignores the name variable in class B while init in C because of super
	#A.__init__(self)
	#B.__init__(self)
 	#pass 
    def getName(self):  
        return self.name  
  
C1 = C()
print help(C1)
print(C1.getName())  
