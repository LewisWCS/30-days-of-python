#tuple is a list that cannot be edited at all

empty_tuple = ()
empty_tuple = tuple()

#tuple uses () instead of [](a list)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
#fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

tuples = ()
brothers = ('Danny','Greg','Bob','Alex')
sisters = ('Megan','Heather','Nikki')
siblings = brothers + sisters
print(siblings)

lst = list(siblings)
lst.insert(0,'Mother')
lst.insert(1,'Father')
family = tuple(lst)
print(family)


