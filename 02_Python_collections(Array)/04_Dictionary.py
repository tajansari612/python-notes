#A dictionary in Python is a data structure that stores the value in
# value:key pairs.

#creating dictionary
dict1  = {
    "name":"taj",
    "rollNo":14,
    "mark":6.85,
    "isPassed":True
};
print(dict1);
print(type(dict1));
print();

#IMP notes
#01 Dictionary items are ordered 
print(dict1);         
print();

#02 Indexing is not possible in Dictionary instead key is used
print(dict1["name"]);
print(dict1["rollNo"]);
print(dict1["mark"]);
print();

#03 Dictionary items are mutable
dict1["name"] = "ayaj";
dict1["rollNo"] = 15;
dict1["mark"] = 8.55;
print(dict1);
print();

#04 Duplicate key's are not allowed but duplicate values are allowed
dict2 = {2:"taj",2:"ayaj"};
print(dict2);         #returns only last key : value pair
dict2 = {1:"taj",2:"taj"};
print(dict2);        #returns all the values
print();

#05 All the datatypes can be stored in list

#06 list items may have diffrent datatypes


#IMP Set Methods
#01 len(dict_name);  //returns the length of dictionary
print(len(dict1));

#02 dict_name.keys();  //return all the keys
print(dict1.keys());
print(type(dict1.keys()));
l1 = list(dict1.keys());
print(l1);
print();

#03 dict_name.values();  //return all the values
print(dict1.values());
print(type(dict1.values()));
l1 = list(dict1.values());
print(l1);
print();

#04 dict_name.pop(key);  //removes the item with a key
print(dict1);
dict1.pop("rollNo");
print(dict1);
print();

#05 dict_name.popitem();  //removes the last item
print(dict1);
dict1.popitem();
print(dict1);
print();

#06 dict_name.clear();  //remove all the items
print(dict1);
dict1.clear();
print(dict1);
print();

#iterating through dictionary
dict1  = {
    "name":"taj",
    "rollNo":14,
    "mark":6.85,
    "isPassed":True
};
for x in dict1:
    print(x," : ",dict1[x]);  # here x represents keys

print("----------------");
for x,y in dict1.items():    # here x represents keys and y repersents values
    print(x,y);


