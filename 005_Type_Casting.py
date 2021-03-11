# Type Casting in python
# Created By: Sandeep Sharma 11-Mar-2021

## It is a way to convert variable of one data type to the another

numStr = '1234' # is this an integer - answer is NO because it is in the single quote so it is a string
print(type(numStr)) # <class 'str'>

num = int(numStr) # this will convert the string to an integer if it is valid to convert
print(num, type(num))

# print(int('str')) => this will give an error as 'str' is not valid to be converted

# Similarly
print(float(1234)) # 1234.0
print(str(1234.0)) # '1234.0'
print(int(1234.5)) # 1234 as will round it to the nearest integer