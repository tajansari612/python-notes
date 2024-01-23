# Python Functions is a block of statements that return the specific task.
# The idea is to put some commonly or repeatedly done tasks together and
# make a function so that instead of writing the same code again and again
# for different inputs, we can do the function calls to reuse code
# contained in it over and over again.

# Some Benefits of Using Functions
# Increase Code Readability 
# Increase Code Reusability

# The syntax to declare a function is:
''' def function_name(parameter1,parameter2,.....,parameterN):
        //statements
        return expression;
'''

# There are mainly two types of functions in Python.
# Built-in library function: These are Standard functions in Python that are available to use.
# User-defined function: We can create our own functions based on our requirements.


# A simple Python function
def func():
    print("Welcome to Python");

# Driver code to call a function
func();

# Types of Parameters
#01 Positional arguments
def sum(a,b):
    print(a,b);
    return a+b;
sum(7,9);     #7 assigned to a & 9 to b

# 02 default parameters
def add(a=0,b=0,c=0):
    print(a,b,c);
    sum = a+b+c;
    return sum;

print(add(4,7,8));
print(add(4,8));
print(add(8));
print(add());

#03 keyword argument
print(add(b=4,c=7,a=9));

#04 Arbitrary argument
def Addition(*args):
    # print(type(args));   # tuple
    sum = 0;
    for i in args:
        sum+=i;
    return sum;

print(Addition(8,7,3,5,6));
print(Addition(8,7,3,5,6,3,6,89));
print(Addition(8,7));