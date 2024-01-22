#Conditionals

#01 if-else statements
num = 78;
if(num%2==0):
    print("It is a even number");
else:
    print("It is odd number")

#02 elif
num = 87;
if(num > 100):
    print("Greater than 100");
elif(num > 50):
    print("Greater than 50");
else:
    print("less than 50");


#03 match case
num1 = int(input("Enter first number :"));
num2 = int(input("Enter second number :"));
Operator = str(input("Enter the operator :"));
match Operator:
    case '+':
        print(num1+num2);
    case '-':
        print(num1-num2);
    case '*':
        print(num1*num2);
    case '/':
        print(num1/num2);
    case _ :
        print("Enter a valid operator");


#loops
#01 for loop
for i in range(1,10,2):    #range(start,end,step)
    print(i);

l1 = [1,5,7,3,4,9];
for i in l1:     
    print(i);
print()

for i in reversed(l1):  #in reverse order
    print(i);
print()

#02 while loop
i = 0;
while(i<10):
    print(i);
    i+=1;