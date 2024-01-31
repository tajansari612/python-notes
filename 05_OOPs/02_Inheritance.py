#One of the core concepts in object-oriented programming (OOP) languages is inheritance.
# It is a mechanism that allows you to create a hierarchy of classes that share 
# a set of properties and methods by deriving a class from another class. Inheritance 
# is the capability of one class to derive or inherit the properties from another class. 

class Student:
    
    def __init__(self,name,rollNo,marks):
        self.name = name;
        self.rollNo = rollNo;
        self.marks = marks;
    
    def getName(self):
        return self.name;
    
    def getRollNo(self):
        return self.rollNo;
    
    def getMarks(self):
        return self.marks;
    
class BE_Student(Student):
    def __init__(self,name,rollNo,marks,isPlaced):
        super().__init__(name,rollNo,marks);
        self.isPlaced = isPlaced;
        
    def getPlacementDetails(self):
        return self.isPlaced;


taj = BE_Student("Taj",14,76,True);
print(taj.getName());
print(taj.getRollNo());
print(taj.getMarks());
print(taj.getPlacementDetails());


#Types of Inheritence
#01 Single Inheritance (one parent and one children)
#02 Mulitple Inheritance (two or more parents and one children)
#03 Multilevel Inheritance (one grand parent,one parent,one children and so on)
#04 Hierarchical Inheritance (one parent and multiple childrens)
#05 Hybrid Inheritance (Multiple types of inheritance is envolved)