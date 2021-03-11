# Varables and Data-Types in python
# Created By: Sandeep Sharma 11-Mar-2021

# variables => a name give to a memory location in a program (name of the variables should not be a reserved keyword in python)
# Examples:

firstName = "Sandeep"   # String data type
secondName = "Sharma"

age = 23 # Integer data type

iAmGood = True # Boolean data type

something = None # None data type

randomNumber = 45.45 # Floating point number data type              # python automatically detects the type of a variable

'''
* valid variable names - str, _str, _str_, str8, st8r etc
* invalid variable names -
    1. def -> reserved keyword
    2. 8str -> var must start with a letter or underscore(_)
    3. str 8 -> no spaces allowed
    4. str@ -> only integers, letters and _ allowed in a name
'''

'''
Primary data types: 
1. Integers -> non-decimal numbers
2. String -> Single quote, double quote, triple quote
3. Boolean
4. Floating point numbers/ Decimal numbers
5. None
'''

# To get a type of a variable
print(type(age)) # prints => <class 'int'>