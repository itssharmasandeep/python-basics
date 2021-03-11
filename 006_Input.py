# Input in python
# Created By: Sandeep Sharma 11-Mar-2021

# Suppose instead to writing by yourself, you want to take some inputs from user then you can use input() in python
# Examples

# Eg-1: take name as input and print it out

name = input('Please enter you name: ')
print('Your name is:', name)


# Eg-2: take an integer number as input and print it's square

num = input('Please enter an interger: ')
print(type(num)) # <class 'str'>
numInt = int(num) # this line is there as whatever we take input from console it will always be a string
print('Square of',num, 'is:', numInt*numInt)