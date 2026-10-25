x = len('python')
y = len('dragon')
print('python is biiger than dragon:', x >y)
print('There is the letter o and n in python and dragon:', 
      'on' in 'python' and 'on' in 'dragon')

print('_jargon_' in '_I hope this course is not full jargon_')

print('There isnt on in python and dragon:',
      'on' not in 'python' and 'on' not in 'dragon')

length = len('_python_')
length = float(length)
length = str(length)
print(float(length), type(length))

number = int(input('Please enter a number: '))
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

print(7 // 3 == 2.7)
print('10' == 10)
print(int(float(('9.8'))) == 10)