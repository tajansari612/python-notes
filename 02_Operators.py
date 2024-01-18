#Operators

#Arithmatic Operators
num1 = 10;
num2 = 20;

#01 Addition
addition = num1 + num2;
print(addition);
print();

#02 Subtraction
subtraction = num2 - num1;
print(subtraction);
print();

#03 Multiplication
multiplication = num1 * num2;
print(multiplication);
print();

#04 Division
division = num2 / num1;
print(division);
print();


#Relational Operators (<,>,==,!=,<=,>=)
num1 = 7;
num2 = 9;

#01 Less than
lessThan = num1 < num2;
print(lessThan)
print();

#02 Greater than
greaterThan = num1 > num2;
print(greaterThan)
print();

#03 Equal to
equalTo = num1 == num2;
print(equalTo);
print();

#04 Not Euqual to
notEqualTo = num1 != num2;
print(notEqualTo);
print();

#05 Less than or equal to
lessThanEqualTo = num1 <= num2;
print(lessThanEqualTo)
print();

#06 Greater than or equal to
greaterThanEqualTo = num1 >= num2;
print(greaterThanEqualTo)
print();


# Logical Opeators (and,or,not)
bool1 = True;
bool2 = False;

#01 Logical and
andOp = bool1 and bool2;
print(andOp);
andOp = bool1 & bool2;
print(andOp);
print();

#02 Logical or
orOp = bool1 or bool2;
print(orOp);
orOp = bool1 | bool2;
print(orOp);
print();

#03 Logical not
notOp = not bool1;
print(notOp);
print();


# Bitwise Operator (&(and),|(or),~(not),^(xor),>>(right shift),<<(left shift))
num1 = 3;  #0011
num2 = 2;  #0010

#01 Bitwise and
bitAnd = num1 & num2; #both 1 then 1 otherwise zero
print(bitAnd);
print();

#02 Bitwise or
bitOr = num1 | num2; #both zero then zero otherwise one
print(bitOr);
print();

#03 Bitwise xor
bitXor = num1 ^ num2;  # both same then zero otherwise one
print(bitXor);
print();

#04 Left Shift
leftShift = num1<<3;  # multiply by 2^3
print(leftShift);
leftShift = num2<<2;  # multiply by 2^2
print(leftShift);
print();

#05 Right Shift
num1 = 24;
rightShift = num1>>3;  # divide by 2^3
print(rightShift);
num2 = 8;
rightShift = num2>>2;  # divide by 2^2
print(rightShift);




