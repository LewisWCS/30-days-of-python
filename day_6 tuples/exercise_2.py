tuples = ()
brothers = ('Danny','Greg','Bob','Alex')
sisters = ('Megan','Heather','Nikki')
siblings = brothers + sisters
lst = list(siblings)
lst.insert(0,'Mother')
lst.insert(1,'Father')
family = tuple(lst)
print(family)

lst = list(family)
parents,siblings = lst[0:2],lst[-3:]
print(siblings)
print(parents)

fruits = ('apple','oranges','apple')
vegetables = ('broccoli','tomatoe','carrot')
animal_products = ('cheese','egg','beef')

food_stuff = fruits + vegetables + animal_products
food_stufff = list(food_stuff)
middle_index = len(food_stufff) // 2
middle_item = food_stufff[middle_index]
print(middle_item)

first_three,last_three = food_stufff[0:3],food_stufff[-3:]
print(first_three)
print(last_three)

food_tuple = list(food_stufff)
del food_tuple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)



