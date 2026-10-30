person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
middle_index = len(person['skills']) // 2
middle_skill = person['skills'][middle_index]
if 'skills' in person:
    print('This is the middle skill:', middle_skill)
else:
    print('Its not in the dictionary')

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python is apart of the skill set')
    else:
        print('Python is not apart of the skills')
else:
    print('There is no skills in the dictionary')

skills = person['skills']
if skills == ['JavaScript', 'React']:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('Unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(f'{person['first_name']} {person["last_name"]} lives in {person["country"]}. He is married.')


    

