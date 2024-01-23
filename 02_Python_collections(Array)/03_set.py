#A Set in Python programming is an unordered collection data type
# that is iterable, mutable and has no duplicate elements.

#creating set
s1 = {1,3,5,7,9,4,3,2,5};
s2 = {"taj","ayaj","raj","pravin"};
print(s1);
print(s2);
print(type(s1));
print();


#IMP notes
#01 set items are unordered 
print(s2);         # Each time you run it different result is shown

#02 Indexing is not possible in set

#03 set items are immutable

#04 Duplicate values are not allowed

#05 All the datatypes can be stored in list

#06 list items may have diffrent datatypes


#IMP Set Methods
#01 len(set_name);  //returns the length of list
print(len(s2));

#02 set_name.add(item);   //add item in the set
s1 = {3,6,4,5,8,9};
print(s1);
s1.add(1);
s1.add(2);
s1.add(7);
s1.add(9);
s1.add(9);
s1.add(9);
print(s1);

#03 set_name.remove(item);   //remove item from the set
s1 = {3,6,4,5,8,9};
print(s1);
s1.remove(6);
s1.remove(9);
s1.remove(3);
#s1.remove(12);   #throw an error
s1.discard(12)    #this will not error
print(s1);

#04 set1.union(set2)  //returns the union of set1 and set2
s1 = {1,2,3,3,4};
s2 = {2,3,3,4,5,6};
s1 = s1.union(s2);
print(s1);

#05 set1.intersection(set2)  //returns the intersection of set1 and set2
s1 = {1,2,3,3,4};
s2 = {2,3,3,4,5,6};
s1 = s1.intersection(s2);
print(s1);

#06 set1.symmetric_difference(set2)  //returns the distinct items  from set1 and set2
s1 = {1,2,3,3,4};
s2 = {2,3,3,4,5,6};
s1 = s1.symmetric_difference(s2);
print(s1);
print();

#iterating through set
s1 = {9,8,4,5,7,4,3,27};
for i in s1:
    print(i);
print();