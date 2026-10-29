dog = {}
dog['Name'] = 'Teddy'
dog['Color'] = 'Golden'
dog['Breed'] = 'Cockapoo'
dog['Legs'] = 'Four'
dog['Age'] = 2
print(dog)

student = {'First_Name':'Lewis','Second_Name':'White','Gender':'Male'
,'Age':'22','martial_status':'single','Skills': ['Gaming','coding','math'],
'Country':'England','City':'St Helens','Address':'Sky Plaza'        
 }
print(len(student))
print(student['Skills'])
print(type(student['Skills']))
student['Skills'] = ['Gaming','coding','math','looks']
student_keys = student.keys()
print(student_keys)
student_values = student.values()
print(student_values)
print(student.items())
del student['First_Name']
print(student)
del student
