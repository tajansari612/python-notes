# The word polymorphism means having many forms. In programming, polymorphism 
# means the same function name (but different signatures) being used for 
# different types. The key difference is the data types and number of 
# arguments used in function

class Animal:
    def speak(self):
        pass;
    
class Dog(Animal):
    def speak(self):
        print("Bhau");
        
class Cat(Animal):
    def speak(self):
        print("Meon");
        
class Cow(Animal):
    def speak(self):
        print("Mooo");
        
dog = Dog();
cat = Cat();
cow = Cow();

cat.speak();
dog.speak();
cow.speak();


# Types of polymorphism

#A) Compile time polymorphism(Resolved during compile time)
#Achieved through
#01 Function Overloading (Method overloading)
#02 Operator Overloading

#B) Run Time Polymorphism (Resolved during run time)
#Achieved through 
#01 Method overiding
