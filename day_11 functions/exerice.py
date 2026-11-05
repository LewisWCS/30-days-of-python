def add_two_numbers(num1,num2):
    sum = num1 + num2
    print(sum)
add_two_numbers(8,9)

def area_of_a_circle(n):
    area = (n ** 2) * 3.14
    print(area)
area_of_a_circle(5)

def add_all_sums(*args):
    for item in args:
        if not isinstance(item, (int,float)): #checks if the item is and interger or float becaseu you cant sum a string with an interger
            print('Not a number')
            return
    total = sum(args)
    print(total)
add_all_sums(4,7,4,65,7)

def conver_celsius_to_fah(c):
    fah = (c * 9/5) + 32
    print(fah)
conver_celsius_to_fah(30)

def check_sesason(m):
    if m in range(0,4):
        print('spring')
    elif m in range(3,7):
        print('Summer')
    elif m in range(6,10):
        print('Autumn')
    elif m in range(9,13):
        print('Winter')
    else:
        print('Number not between 0-12')
check_sesason(9)

def calculate_slope(x1,x2,y1,y2):
    slope = (y2 - y1) - (x2 - x1)
    print('The slope will be:', slope)
calculate_slope(5,7,9,5)

import math

def quadratic_form(a,b,c):
    discrim = (b**2) - 4 * a * c

    x1 = (-b + math.sqrt(discrim)) / (2 * a)
    x2 = (-b - math.sqrt(discrim)) / (2 * a)

    return(x1,x2)

print(quadratic_form(1,-5,6))

def print_list(list):
    for i in list:
        print(i)

print_list(['Lewis','Megan','Mother'])

def reverse_list(list):
    lst = []
    for i in list:
        lst.insert(0, i)
    return(lst)
print(reverse_list(['Lewis','Megan','Mother']))

def last_index(n):
    last = len(n) - 1
    return(last)

def capa_list(list):
    lst=[]
    for i in list:
        i = i.upper()
        lst.insert(last_index(list), i)
    return lst
print(capa_list(['lewis','megan','mother']))
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
numbers = [2, 3, 7, 9];

def add_item(my_list,item):
    my_list.append(item)
    return my_list

print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]


numbers = [2, 3, 7, 9]
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']


def remove_item(my_list,item):
    my_list.remove(item)
    return my_list

print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
print(remove_item(numbers, 3))  # [2, 7, 9]  


def sum_of_number(n):
    total = 0
    for i in range(n + 1):
        total = total + i  
    return total
print(sum_of_number(10))

def sum_of_even(n):
    total = 0 
    for i in range(n+1):
        if i % 2 == 0:
            total = total + i 
        else:
            continue
    return total
print(sum_of_even(10))

def even_and_odds(n):
    even_numbers = 0
    odd_numbers = 0
    for i in range(n+1):
        if i % 2 == 0:
            even_numbers = even_numbers + 1 
        else:
            odd_numbers = odd_numbers + 1 
    print('The amount of even numbers are', even_numbers)
    print('The amount of odd numbers are', odd_numbers)
even_and_odds(10)

def is_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False

print(is_empty([]))


def calculate_mean(*args):
    for i in range(len(args)):
        return sum(args) / len(args)

print('The mean of the list of numbers',calculate_mean(20,10,30,30,20))

def calculate_medium(*args):
    number = sorted(args)
    middle_index = int(len(number) / 2)
    for i in range(len(number)):
        return number[middle_index]

print('The middle index is', calculate_medium(10,9,5,6,7,8,9))

def calculate_mode(*args):
    mode = args[0]
    highest_count = 0

    for num in args:
        count = args.count(num)
        if count > highest_count:
            highest_count = count
            mode = num
    return mode
print('The mode of the list is', calculate_mode(2,3,4,5,6,7,8,8))
def range_calc(*args):
    number = sorted(args)
    last_index = len(args) - 1
    range = number[last_index] - number[0]
    return range
print('The range of the list is', range_calc(2,4,5,6,1,5,6,7,9))

def greet(n=''):
    if n != '':
        print(f'Hello , {n}')
    else:
        print('Hello, guest')
greet()
greet('Lewis')

def show_args(**args):
    print('Recieved:', end='')
    for keys,value in args.items():
        print(f'{keys}: {value}', end =', ')
show_args(Name = 'Lewis',Age = 22, Uni = 'Uni Of Leeds')
                


    

