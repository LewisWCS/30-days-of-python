# syntax
#for iterator in lst:
    #code goes here
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
# using a for loop on a string
# syntax
#for iterator in string:
    #code goes here
language = 'Python'
for letter in language:
    print(letter)

    # or

for i in range(len(language)):
    print(language[i])
#for loop on a tuple
# syntax
#for iterator in tpl:
    #code goes here
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
#for loop in dictionary
  # syntax
#for iterator in dct:
    #code goes here
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
#Using for loop in set
# syntax
#for iterator in st:
    #code goes here
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
#break part 2 
# syntax
#for iterator in sequence:
    #code goes here
    #if condition:
        #break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
#continue for loop part 2 
  # syntax
#for iterator in sequence:
    #code goes here
    #if condition:
        #continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
# the range function
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2)) # counts in twos until it reaches the last number before 11
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
# range function part 2 
# syntax
#for iterator in range(start, end, step):
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
#nested for loop
# syntax
for x in y:
    for t in x:
        print(t)
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
# A for else loop 
# syntax
#for iterator in range(start, end, step):
    #do something
#else:
    #print('The loop ended')
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
#pass
for number in range(6):
    pass