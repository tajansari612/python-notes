# Access modifiers are used by object oriented programming languages like C++,
# java,python etc. to restrict the access of the class member variable and 
# methods from outside the class. Encapsulation is an OOPs principle which 
# protects the internal data of the class using Access modifiers like Public,
# Private and Protected.

#01 Public Access Modifier
# By default the member variables and methods are public which means they 
# can be accessed from anywhere outside or inside the class. No public keyword 
# is required to make the class or methods and properties public

#02 Private Access Modifier
# Class properties and methods with private access modifier can only be 
# accessed within the class where they are defined and cannot be accessed 
# outside the class. In Python private properties and methods are declared by 
# adding a prefix with two underscores(‘__’) before their declaration

class BankAccount:
   def __init__(self, account_number, balance):
      self.__account_number = account_number
      self.__balance = balance
    
   def __display_balance(self):
      print("Balance:", self.__balance)

b = BankAccount(1234567890, 5000)
# b.__display_balance()    #Error


#03 Protected Access Modifier
# Class properties and methods with protected access modifier can be accessed 
# within the class and from the class that inherits the protected class. 
# In python, protected members and methods are declared using single 
# underscore(‘_’) as prefix before their names.
class Person:
   def __init__(self, name, age):
      self._name = name
      self._age = age
    
   def _display(self):
      print("Name:", self._name)
      print("Age:", self._age)

class Student(Person):
   def __init__(self, name, age, roll_number):
      super().__init__(name, age)
      self._roll_number = roll_number
    
   def display(self):
      self._display()
      print("Roll Number:", self._roll_number)

s = Student("John", 20, 123)
s.display() 
p = Person("taj", 24)
p._display();