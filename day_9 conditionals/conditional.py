# syntax
# 
# if condition:
# this part of code runs for truthy conditions
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
# this is an if with an else
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# This is and elof statment used to have multiple elements to check if its wrong
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
# can be nested if statments, so if statments can be in if statements
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
#
#  this is and if statment with two conditions join with an and
# # syntax
if condition and condition:
    code
#This is an if statment with an or
# syntax
if condition or condition:
    code
