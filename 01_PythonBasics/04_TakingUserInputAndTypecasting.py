#Taking user input
# name = input("Enter your name :");
# print("Hello ,"+name);


#Typecating

#01 integer to string
num = 123;
str1 = str(num);
print(str1);
print(type(str1));
print();

#02 string to integer
str2  = "1345";
num = int(str2);
print(num);
print(type(num));
print();

#03 list to tuple
l1 = [1,2,3,4,5];
print(l1);
print(type(l1));
t1 = tuple(l1);
print(t1);
print(type(t1));
print();

#04 tuple to list
t1 = (1,2,3,4,5);
print(t1);
print(type(t1));
l1 = list(t1);
print(l1);
print(type(l1));
print();

#05 string to list
str = "Hello World!";
print(str,type(str));
l1 = list(str);
print(l1,type(l1));
print();

#06 list to string
# print(l1,type(l1));  #error
# str = str(l1);
# print(str,type(str));