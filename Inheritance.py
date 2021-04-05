# A Python program to demonstrate inheritance 
  

class Parent(object):
      
    # Constructor
    def __init__(self, name):
        self.name = name
  
    # To get name
    def getName(self):
        return self.name
  
  
# Inherited or Sub class 
class Child(parent):
      
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
  
    # To get name
    def getAge(self):
        return self.age
  
# Inherited or Sub class 
class GrandChild(Child):
      
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
  
    # To get address
    def getAddress(self):
        return self.address        
  
# Driver code
obj1 = GrandChild("Akash", 23, "Hyderabad")  
print(obj1.getName(), obj1.getAge(), obj1.getAddress())