strings = ' '.join(['Thirty', 'Days', 'Of','Python'])
print(strings)
coding = ' '.join(['Coding','For','All'])
print(coding)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())

string = '_Coding For All_'
print(string.capitalize().title().swapcase())

first_word = string[:7]
print(first_word)

string = 'Coding For All'
string_2 = string.replace('Coding', 'Python')
print(string_2)

x = 'Python for everyone'
print(x.replace('everyone','All'))

string = 'Coding For All'
string = string.split(' ')
print(string)

string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(','))

character = '_Coding For All_'
first_letter = character[0]
print(first_letter)
last_index = len(character) - 1
last_letter = character[last_index]
print(last_letter)
letter10 = character[10]
print(letter10)

character = 'Coding For All'
ten = character[10]
print(ten)

character = 'Python For Everyone'
acronym = ' '.join(word[0] for word in character.split())
print(acronym)

character = 'Coding For All'
acronym = ' '.join(word[0] for word in character.split())
print(acronym)

character = 'Coding For All'
position = character.index('C')
print(position)

character = 'Coding For All'
position = character.index('F')
print(position)

character = 'Coding For All People'
position = character.rfind('l')
print(position)

character = 'You cannot end a sentence with because because ' \
'because is a conjunction'
position = character.find('because')
print(position)

character = 'You cannot end a sentence with because because because is a conjunction'
position = character.rfind('because')
print(position)

character = 'You cannot end a sentence with because because ' \
'because is a conjunction'
phrase = character[31:54]
print(phrase)

character = 'You cannot end a sentence with because because ' \
'because is a conjunction'
position = character.find('because')
print(position)

character = 'You cannot end a sentence with because because ' \
'because is a conjunction'
phrase = character[31:54]
print(phrase)

character = 'Coding For All'
print(character.startswith('Coding'))
print(character.endswith('coding'))

character = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
character = character.replace('&nbsp;', ' ')
character = character.strip().lstrip().rstrip()
print(character)

x = '30DaysOfPython'
print(x.isidentifier())
x = 'thirty_days_of_python'
print(x.isidentifier())

library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
var = ' '.join(library)
print(var)

print('I am enjoying this challenge. \nI just wonder whats next.')

print('Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with a radius of {} is {:.0f}'.format(radius,area))

x = 8
y = 6
print(f'{x} + {y} = ', x + y)
print(f'{x} - {y} = ', x - y)
print(f'{x} * {y} = ', x * y)
print(f'{x} / {y} = {x / y:.2f}')
print(f'{x} % {y} = ', x % y)
print(f'{x} // {y} = ', x // y)
print(f'{x} ** {y} = ', x ** y)
