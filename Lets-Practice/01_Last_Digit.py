# Practice Question 1
# Created By: Sandeep Sharma 11-Mar-2021

#Question : Input an integer number from user and find the last digit of that integer number. Assume that number is positive interger.
# Eg: if number is 1234 then output should be 4 as 4 is the last digit

#Solution:
# So for this we will use % (modulus) operator
# a%b = remainder of a after dividing by b where a and b are integers
# So if we take a % 10 then it will give us the last digit as that will be remainer after dividing by 10

num = input('Enter a number: ')
num = int(num) # as initially it would be string
lastDigit = num % 10
print('Last digit of number',num,'is:',lastDigit)
