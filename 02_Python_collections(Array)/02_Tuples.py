#Python Tuple is a collection of objects separated by commas.
# In some ways, a tuple is similar to a Python list
# in terms of indexing, nested objects, and repetition but
# the main difference between both is Python tuple is immutable,
# unlike the Python list which is mutable.

#creating tuple
l1 = (1,3,5,7,9,4,3,2,5);
l2 = ("taj","ayaj","raj","pravin");
print(l1);
print(l2);
print(type(l1))
print();

#IMP notes
#01 Tuples items are indexed
print(l2[0]);
print(l2[1]);   #Positive indexing
print(l2[2]);   #Positive indexing
print(l2[-1]);   #Negative indexing  gives last element
print(l2[-3]);   #Negative indexing  gives 3rd last element
print(l1[2:6]);   #Range indexing
print();

#02 Oredered means in which order items are inserted they follow the same order

#03 Tuple items are immutable means it can not be changed
# l2[2]="gopi";   //error
# print(l2[2]);
print();

#04 Duplicate values are allowed in list

#05 All the datatypes can be stored in list
l3 = (True,False,False,True);
print(l3);
print();

#05 list items may have diffrent datatypes
l4 = (1,34.5,True,"Taj");
print(l4);
print();

#06 Tuples are faster than Lists