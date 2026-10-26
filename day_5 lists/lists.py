lst = []
empty_list = []
print(len(empty_list))

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

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

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

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit,second_fruit,third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)


