import os
		
#definition of the class starts here  
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
    def getId(self):                  ########################CHECK THIS and order of the class in the derived class(Student,person line30)
        return (self.age)  
    #end of class definition  
  
# defining another class  
class Student: # Person is the  
    def __init__(self, studentId,name):  
        self.studentId = studentId  
	self.name = name
  
    def getId(self):  
        return self.name
  
  
class Resident(Person,Student): # extends both Person and Student class  
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id, "Hardik")  
  
# Create an object of the subclass  
resident1 = Resident('John', 30, '102')  
resident1.showName()  
print(resident1.getId())
