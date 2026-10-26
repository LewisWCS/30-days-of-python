lst = []
empty_list = []
print(len(empty_list))
# tell you the length
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 
print('Number of friuts:', len(fruits))
print('Number of vegetables:', len(vegetables))
print('Number of animal products:', len(animal_products))
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))
#different types of list
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
# how to print a sepcific index
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
third_fruit = fruits[2]
print(third_fruit)
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)
# puts the list into individual strings/varibles
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit,second_fruit,third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
#print a specific range of varibels 
fruits = ['banana', 'orange', 'mango','lemon']
all_fruits = fruits[0:4]
print(all_fruits)
orange_and_mango = fruits[1:3] # start at index 1 stop at index 3
print(orange_and_mango)
#changes a certain index value with the one you assign 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)
# checking if its in there using bool values True and False
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)
# places a varible in the list at the very end of the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)
#insert a varibe in a specific spot
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
fruits.insert(3, 'lime')
print(fruits)
#remove a string from the list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
fruits.remove('lemon')
print(fruits)
# removes a certain index but if it undefined the last one
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)
# deleitng a string and can adjust what one to remove using index
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[1:3]
print(fruits)
#copies the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)
#adds mulirple lists together/ order matters
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# different way of adding lists
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# counts how many strings are in that list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
#tells you the index of the string you typed
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
# reverses the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
# sorts it into aplhabetic order or can do revers if you do reverse = true
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
# sorts the list wiht changing the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana'