# In Python, object-oriented Programming (OOPs) is a programming paradigm that
# uses objects and classes in programming. It aims to implement real-world
# entities like inheritance, polymorphisms, encapsulation, etc. in the 
# programming. The main concept of OOPs is to bind the data and the functions 
# that work on that together as a single unit so that no other part of the code 
# can access this data.

# Why to use OOPs in python
#01 Helps to mimic real world entities and their properties
#02 Code reausablility
#03 Organization and maintainability of code


#OOPs Concepts in Python
#01 Class
#02 Objects
#03 Class Constructor
#04 Polymorphism
#05 Encapsulation
#06 Inheritance
#07 Data Abstraction


#01 Class
# A class is a collection of objects. A class contains the blueprints or the 
# prototype from which the objects are being created. It is a logical entity 
# that contains some attributes and methods. 

class student :
    def setInfo(self,name,rollNo,marks):
        self.name = name;
        self.rollNo = rollNo;
        self.marks = marks;
    
    def getName(self):
        return self.name;
    
    def getRollNo(self):
        return self.rollNo;
    
    def getMarks(self):
        return self.marks;
        

#02 Objects
#The object is an entity that has a state and behavior associated with it.
# It may be any real-world object like a mouse, keyboard, chair, table, pen, etc.
# Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects

taj = student();
taj.setInfo("Taj",14,76);
ayaj = student();
ayaj.setInfo("Ayaj",15,86);

print(taj.getName());
print(taj.getRollNo());
print(taj.getMarks());
print();

print(ayaj.getName());
print(ayaj.getRollNo());
print(ayaj.getMarks());
print();


#03 Class Constructor
#The __init__ method is similar to constructors in C++ and Java. It is run as 
# soon as an object of a class is instantiated. The method is useful to do any 
# initialization you want to do with your object.

class Rectangle:
    def __init__(self,height,width):
        self.height = height;
        self.width = width;
        
    def getArea(self):
        return self.height*self.width;
    
    def getPerimeter(self):
        return 2*(self.height+self.width);
    
rectangle1 = Rectangle(8,9);
print(rectangle1.getArea());
print(rectangle1.getPerimeter());