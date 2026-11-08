from string import *
from random import *

def random_user_id():
    for i in range(1,7):
        if i == 1 or i == 4 or i == 5:
            print(choice(digits),end='')
        else:
            print(choice(ascii_lowercase),end='')

random_user_id()

def user_id_gen_by_user(n,k):
    for i in range(n):
        for j in range(k):
            print(choice(digits + ascii_lowercase), end='')
        print()

user_id_gen_by_user(5,5)

def rgb_color_gen():
    print(f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})')

rgb_color_gen()

def list_of_hexa():
    every = digits + 'abcdef'
    print('#', end='')
    for i in range(6):
        print(choice(every),end='')

list_of_hexa()

