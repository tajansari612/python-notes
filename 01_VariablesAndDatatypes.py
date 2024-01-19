#Variables
#Variables are containers for storing data values.

#Python has no command for declaring a variable.

#A variable is created the moment you first assign a value to it.

#Python is Dynamically typed Prgoramming Language means it chooses
#the datatype of the variable dynamically itself


# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

print("Hello!")

var1 = "Taj"
var2 = "Raj"
print(var1)
print(var2)

var1 = "Ayaj"
var3 = var2
print(var1)
print(var3)
print();
#Data Types 

#01 Integer
num1 = 12;
num2 = 13;
sum = num1 + num2;
print(sum)
print(type(sum))

#02 Float
num3 = 12.54
num4 = 34.67
print(num4-num3)
print(type(num4-num3))

#03 Boolean
isLoggedIn = True
val = False
print(isLoggedIn)
print(val)
print(type(val))

#04 Char
ch1 = 'T'
ch2 = 'A'
ch3 = 'J'
print(ch1)
print(ch1+ch2+ch3)
print(type(ch2))    #Python does not have character data type
ch2 = ch2 + ch3;
print(ch2)

#05 String
str1 = "Taj"
str2 = "Ansari"
print(str1+str2)
print(type(str2))

#06 Complex
num1 = 3 + 4j;       # In the python j is used instead of i
num2 = 4 + 3j;
num3 = num1 + num2;
print(num3);
print(type(num3))

#07 List
#Python Lists are just like dynamically sized arrays, 
# declared in other languages (vector in C++ and ArrayList in Java).
# In simple language, a list is a collection of things, enclosed in [ ] and separated by commas. 
l1 = [1,3,5,7,9,4,3,2,5];
l2 = ["taj","ayaj","raj","pravin"];
print(l1);
print(l2);
print(type(l1))


#08 Tuple
#Python Tuple is a collection of objects separated by commas.
# In some ways, a tuple is similar to a Python list in terms of
# indexing, nested objects, and repetition but the main difference between
# both is Python tuple is immutable, unlike the Python list which is mutable.
#To create a tuple we will use () operators.
t1 = (2,4,6,7,8,9,12);
t2 = ("taj","ayaj","raj","pravin")
print(t1);
print(t2);
t1 = (2,3,5,6)
print(t1)
print(type(t1))
#t1[3] = 9;   #error as it is immutable item cannot be assigned a new value


#09 Dictionary
#A dictionary in Python is a data structure that stores the value in value:key pairs.
dict1 = {
#number : frequency
    5 : 4,
    7 : 3,
    9 : 7,
    8 : 2
}
print(dict1);
dict2 = {
    "rollNo" : 14,
    "Name" : "Taj",
    "Gender" : "Male",
    "Mark" : True
}
print(dict2);
print(type(dict1))


#10 Sets
#A Python set is the collection of the unordered items.
# Each element in the set must be unique, immutable, and
# the sets remove the duplicate elements.
# There is no index attached to the elements of the set, i.e.,
# we cannot directly access any element of the set by the index.
s1 = {2,4,6,7,8,9};
print(s1)
print(type(s1))