challange = 'thirty days of python'
print(challange.count('y'))
print(challange.count('y', 7, 14)) # 7 ,14 is the range
print(challange.count('th'))
#checks if it ends with a certain string
print(challange.endswith('on'))
print(challange.endswith('tion'))
#expands the tabs
challange = 'thirty\tdays\tof\tpython'
print(challange.expandtabs())
print(challange.expandtabs(10))
#finds the letter occording to index if not returns -1
challange = 'thirty days of python'
print(challange.find('y'))
print(challange.find('th'))
print(challange.rfind('y'))
print(challange.rfind('th'))

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {:.0f}'.format(radius, area)
print(result) # The area of a circle with radius 10 is 314
# substrings
challange = 'thrity days of python'
sub_strings = 'da'
print(challange.index(sub_strings))
print(challange.index(sub_strings, 9))# asking to find it after index 9

print(challange.rindex(sub_strings))
print(challange.rindex(sub_strings, 9))
print(challange.index('on', 8))
#checks for alphanumeric numbers
challange = 'ThirtyDaysOfPython'
print(challange.isalnum()) #true
challange = '30DaysOfPython'
print(challange.isalnum()) #true
challange = 'Thirty Days Of Python' # not true ebcasue it has spaces
#checks string elements that are alphabetic(a-z,A-Z)
challange = 'Thirty Days Of Python'
print(challange.isalpha()) #false becasue spaces are exculded
challange = 'ThirtyDaysOfPython'
print(challange.isalpha())# true
num = '123'
print(num.isalpha())# false because its numbers
# checks if the strings are decimal(0-9)
challenge = 'thirty days of python' #false
print(challange.isdecimal())
challange = '123' #true
print(challange.isdecimal())
challange = '\u00B2' #true
print(challange.isdecimal())
challange = '12 3' #false spaces not allowed
print(challange.isdecimal())
#checking if all characters in string are numbers (0-900 and some 
# other unicode for characters

challenge = 'Thirty'
print(challange.isdigit())#false
challenge = '30'
print(challange.isdigit())#true
challange = '\u00B2' #true
print(challange.isdigit())#true



 

