for i in range(0,11):
    print(i)
count = 0
while count < 11:
    print(count)
    count = count + 1

for i in range(10,-1,-1):
    print(i)
count = 10
while count > -1:
    print(count)
    count = count - 1

for i in range(1,8):
    print('#' * i)

for col in range(8):
    for row in range(8):
        print('#', end=' ') # end =' ' stops it from going on to another line
    print() # makes it go to another line

for i in range(11):
    print(f'{i} * {i} =', i * i)

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item, end=' ')

for i in range(0,101,2):
    print(i, end=' ')

for i in range(101):
    if i % 2 == 0:
        continue
    else:
        print(i, end=' ')