#Python Lists are just like dynamically sized arrays, 
# declared in other languages (vector in C++ and ArrayList in Java).
# In simple language, a list is a collection of things, enclosed in [ ] and separated by commas. 
l1 = [1,3,5,7,9,4,3,2,5];
l2 = ["taj","ayaj","raj","pravin"];
print(l1);
print(l2);
print(l1[2:6]);   #prints elements 2nd,3rd,4th and 5th  (0-based indexing)
print(type(l1))
print();


#IMP notes
#01 List items are indexed
print(l2[0]);
print(l2[1]);
print(l2[2]);
print();

#02 Oredered means in which order items are inserted they follow the same order

#03 list items are mutable means it can be changed
l2[2]="gopi";
print(l2[2]);
print();

#04 Duplicate values are allowed in list

#05 All the datatypes can be stored in list
l3 = [True,False,False,True];
print(l3);
print();

#05 list items may have diffrent datatypes
l4 = [1,34.5,True,"Taj"];
print(l4);
print();


#IMP List Methods
#01 len(list_name);  //returns the length of list
print(len(l4));

#02 list_name.append(item);  //add item at the end
l5 = [1,2,3,4];
print(l5);
l5.append(5);
l5.append(6);
l5.append(7);
print(l5);
print();

#03 list_name.insert(index,item);  //add item at given index and all the item after that pushed forward by 1
l5 = [1,2,3,4];
print(l5);
l5.insert(3,34);
l5.insert(2,26);
print(l5);
print();

#04 list_name1.extend(list_name2); //add list2 to list1
l1 = [1,2,3];
l2 = [5,6,7];
print(l1);
print(l2);
l1.extend(l2);
print(l1);
print();

#05 list_name.pop();  //removes item from the end and if provide index then removes element from that index
l5 = [1,2,3,4,5,6,7,8,9];
print(l5);
l5.pop();
print(l5);
l5.pop();
print(l5);

l5.pop(4);    #removes element from 4th index
print(l5);
print();

#06 list_name.remove(item)  //removes given item
l5 = [11,45,32,76,84,53,66];
l5.remove(45);
print(l5);
l5.remove(76);
print(l5);
# l5.remove(45);  //gives error as element is not present in list 
# print(l5);
print();

#07 list_name.sort()  //sorts items in ascending order
#   list_name.sort(reverse=True)  //sorts items in descending order
l1 = [9,8,4,5,7,4,3,27];
print(l1);
l1.sort();
l1.sort(reverse=True);
print(l1);
print();

# Joining two tuples
l1 = [1,2,3,4];
l2 = [3,4,5,6];
l1 = l1+l2;
print(l1);
print();

#iterating through list
l1 = [9,8,4,5,7,4,3,27];
for i in l1:
    print(i);
print("------");
for i in range(0,len(l1)):
    print(i," ---> ",l1[i]);