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