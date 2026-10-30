
total = 0
for i in range(101):
    total = total + i
print('The sum of all number 0-100:', total)

total = 0 
for i in range(101):
    if i % 2 == 0:
        continue
    else:
        total = total + i
print('The sum of odd intergers from 0-100:',total)