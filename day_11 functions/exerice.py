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

def add_item()

        
