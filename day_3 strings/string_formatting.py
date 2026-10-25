# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.<small>number of digits</small>f" - Floating point numbers with fixed precision


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * (radius**2)
formated_strings = 'The area of a circle is %.2f with a radius of %d.' %(area,radius)
print(formated_strings)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_stringss = 'The following are python libraries: %s'%(python_libraries)
print(formated_stringss)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')