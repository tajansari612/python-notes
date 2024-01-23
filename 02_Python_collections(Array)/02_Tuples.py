#Python Tuple is a collection of objects separated by commas.
# In some ways, a tuple is similar to a Python list
# in terms of indexing, nested objects, and repetition but
# the main difference between both is Python tuple is immutable,
# unlike the Python list which is mutable.

#creating tuple
t1 = (1,3,5,7,9,4,3,2,5);
t2 = ("taj","ayaj","raj","pravin");
print(t1);
print(t2);
print(type(t1))
print();
#IMP notes
#01 Tuples items are indexed
print(t2[0]);
print(t2[1]);   #Positive indexing
print(t2[2]);   #Positive indexing
print(t2[-1]);   #Negative indexing  gives last element
print(t2[-3]);   #Negative indexing  gives 3rd last element
print(t1[2:6]);   #Range indexing
print();

#02 Oredered means in which order items are inserted they follow the same order

#03 Tuple items are immutable means it can not be changed
# t2[2]="gopi";   //error
# print(t2[2]);
print();

#04 Duplicate values are allowed in list

#05 All the datatypes can be stored in list
t3 = (True,False,False,True);
print(t3);
print();

#06 list items may have diffrent datatypes
t4 = (1,34.5,True,"Taj");
print(t4);
print();

#07 Tuples are faster than Lists


#IMP List Methods
#01 len(tuple_name);  //returns the length of list
print(len(t4));

# Joining two tuples
t1 = (1,2,3,4);
t2 = (3,4,5,6);
t1 = t1+t2;
print(t1);


#iterating through tuple
t1 = (9,8,4,5,7,4,3,27);
for i in t1:
    print(i);
print("------");
for i in range(0,len(t1)):
    print(i," ---> ",t1[i]);