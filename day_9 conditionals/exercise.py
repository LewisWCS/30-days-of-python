age = int(input('What is your age: '))
if age >= 18:
    print('You are old enough to drive!')
else:
    print('You need to wait',18 - age,'years before you can drive')

my_age = int(input('What is my age: '))
your_age = int(input('What is your age: '))
if my_age > your_age:
    print('Im older than you by', my_age - your_age,'years')
elif my_age < your_age:
    print('You are older than me by', your_age - my_age,'years')
else:
    print('We are the same age')

num_1 = int(input('Please enter numner A: '))
num_2 = int(input('Please enter numner B: '))
if num_1 > num_2:
    print('A is bigger than B')
elif num_1 < num_2:
    print('A is smaller than B')
else:
    print('A is equal to B')
    