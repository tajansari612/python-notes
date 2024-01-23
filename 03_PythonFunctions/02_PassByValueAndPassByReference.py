# Pass by value
def addTen(num):   #here copy of num is created into new num variable
    num+=10;
    print("Inside function :",num)
    return num;
    
num = 18;
print(num);
addTen(num);
print(num);   # Value num is not affected
print();

# Pass by reference
def modifyList(lst):  #here the reference of list passed so copy is not created
    lst.append(99);
    print("Inside function :",lst);
    return lst;

lst = [1,2,3];
print(lst);
modifyList(lst);  # value changes in list lst
print(lst);
print();