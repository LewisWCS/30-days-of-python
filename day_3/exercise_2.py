x = int(input('Please enter a value of x: '))
y = (2 * x) - 2
print('The slope is:', y)

y1 = 2
y2 = 10
x1 = 2
x2 = 6
slope = (y2 - y1) / (x2 - x1)
print('The slope is', slope)
distance = ((((x2 - x1)**2) - ((y2 - y1)**2)) ** (1/2))
print('The distance is: ', distance)

print('Task 8 is bigger than task 9: ')
if y == slope or y > slope:
    print(True)
else:
    print(False)

x_squared = int(input('Please enter a value for x: '))
y_x = x_squared **2 + 6 * x_squared + 9 
print('The value of y is: ', y_x)
