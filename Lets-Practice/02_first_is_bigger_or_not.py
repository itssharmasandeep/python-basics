# Practice Question 2
# Created By: Sandeep Sharma 11-Mar-2021

#Question : Input two integer numbers and check first is bigger or equal.
# Eg: first: 49 , second: 55 print False because first is smaller than second 
# Eg: first: 55 , second: 55 print True as both equal

#Solution:
# So for this we will use >= operator , there may be other operators and solution as well
# a >= b = a greater than eqauls to b where a and b are integers

num1 = input('Enter first number: ')
num1 = int(num1) # as initially it would be string
num2 = input('Enter first number: ')
num2 = int(num2) # as initially it would be string
check = (num1 >= num2)
print('First number is bigger or equal:', check)
