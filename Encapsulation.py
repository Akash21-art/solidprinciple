# Python program to demonstrate protected members
 
 
# Creating a Parent class
class Parent:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a Child class   
class Child(Parent):
    def __init__(self):
         
        # Calling constructor of Parent class
        Parent.__init__(self)
        print("Calling protected member of parent class: ")
        print(self._a)
 
obj1 = Child()
         
obj2 = Parent()
 
# Calling protected member Outside class will  result in AttributeError
print(obj2.a)