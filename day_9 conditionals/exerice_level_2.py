num = int(input('Please enter a grade 0-100: '))
if num >= 90 and num <=100:
    print('Grade: A')
elif num >= 80 and num <=89:
    print('Grade: B')
elif num >= 70 and num <= 79:
    print('Grade: C')
elif num >= 60 and num <= 69:
    print('Grade: D')
elif num >= 0 and num <= 59:
    ('Grade: F')
else:
    print('You did not enter in the range 0-100')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input('What fruit do you want adding to the list: ')
if fruit_input in fruits:
    print('Its already apart of the list')
else:
    fruits.append(fruit_input)
    print(fruit_input,'has been added!')
    print(fruits)


