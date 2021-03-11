# Operators in python
# Created By: Sandeep Sharma 11-Mar-2021

'''
These following operators are the some common operators in python
1. Arithmetic Operators: +, -, *, /          etc.
2. Assignment Operators: =, +=, *=           etc.
3. Comparison Operators: ==, > ,<,  >=, <=   etc.
4. Logical Operators:    and, or, not        etc.
'''

# Addition of two numbers #####

# use of assignment operator = , to assign values to variables
numA = 55
numB = 44

# use of add + operator, to add two values and then assigning value to a new variable
sumAB = numA + numB 

# to print multiple lines use comma(,) 
print('Addition : ', numA + numB, 'is same as : ', sumAB)

# Other examples of arithmetic operators
print('numA - num B =', numA - numB)
print('numA * num B =', numA*numB)
print('numA / num B =', numA/numB) # this operator will give floating point value even if numA is divisible by numB

# Assignment operators examples

# adding a value to the self
numC = 20
numC += 5 # this is the short form of numC = numC + 5
print('numC :', numC) # here numC will be 25

# similarly we can use *= -= /=

# Comparison operators
# these operators will check the condition and gives back a boolean value -> True or False

check = (4 > 7)
print("This condition 4 > 7 is:", check) # check is False in this case as 4 is not greter than 7

check = (4 == 4) # this is true
check = (4 == 4.0) # this is also true
check = (4 == '4') # this is false as string is being compared with integer/number

# Logical operators
# these operators, operates on booleans

# and => if all booleans are true then true otherwise false
print('This values is:', True and True and True) # this is True
print('This values is:', True and True and False) # this is False

# or => if any boolean is true then true otherwise false
print('This values is:', True or False or False) # this is True
print('This values is:', False or False or False) # this is False

# not => if true then false otherwise true
print('This values is:', not False) # this is True
print('This values is:', not True) # this is False

