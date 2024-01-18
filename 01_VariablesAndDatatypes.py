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



