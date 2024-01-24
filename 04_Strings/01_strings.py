# String is a data structure in Python that represents a sequence of characters.
# It is an immutable data type, meaning that once you have created a string,
# you cannot change it. Strings are used widely in many different applications,
# such as storing and manipulating text data, representing names, addresses, and
# other types of data that can be represented as text.

# Python does not have a character data type, a single character is simply a
# string with a length of 1.

# syntax for creating string
# 01 using single quote
str1 = 'Taj';
print(str1,type(str1));

# 02 using double quote
str2 = "Ayaj";
print(str2,type(str2));

# 03 using triple quote
str2 = '''Raj
 hat bat cat lrij eoe
 cieiejff
 fneifhoo''';        # it used for storing paragraphs which has multiple lines
print(str2,type(str2));


# IMP Notes
#01 Indexing is possible in strings like list
str = "Hello World!";
print(str[0]);
print(str[2]);
print(str[7]);
print(str[-1]);
print(str[-3]);
print();

#02 Strings in python are immutable
# str[0] = 'T';   #Error 
# print(str);

#03 String slicing
print(str[2:5]);   #returns 2nd,3rd and 4th element
print(str[:5]);    #returns elements upto 4th
print(str[2:]);    #return elements from 2nd to last
print();

# IMP Methods
#01 len(strring_name);   #returns the length of the string
print(len(str));
print();

#02 string_name.find(x);    #x could be a character or string
print(str.find('r'));        #returns the first occurence if not present then returns -1
print(str.find('rld!'));
print(str.find('g'));
print();

#03 string_name.upper();  # converts the string into uppercase
str = "hello world!";
print(str.upper());

#04 string_name.lower();  # converts the string into lowercase
str = "HELLO WORLD!";
print(str.lower());

#05 string_name.capitalize();  # converts the first character of string into uppercase
str = "hello world!";
print(str.capitalize());

#06 string_name.replace(old_substring,new_substring,count);  # converts the string into uppercase
str = "hello world!     hello world!    hello world!    hello world!";
print(str.replace("hello","hi"));  #here count is not mentioned so it replaces all the occurences 
print(str.replace("hello","hi",2));  #count = 2 mentioned so it replaces 2 occurences 
print();

#06 string_name.split(sep,maxsplit);   # split the string into list
str = "hi how are you. I am fine. thank you!";
print(str.split(),type(str.split()));  # it split the string with the whitspaces
print(str.split("."));  # it split the string with the .
print(str.split(" ",4));  # it split the string with the whitspace upto 4
print();

#07 String concatenation
str1 = "Hello ";
str2 = "World!";
str3 = str1 + str2;
print(str3);
print()

# Traversing a string
str = "Hello World!";
for i in str:
    print(i);
print();

l1 = list(str);
print(l1,type(l1)); 
