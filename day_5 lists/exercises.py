list = []
list = ['Red','Blue','Green','Purple','Orange']
print(len(list))

first_item = list[0]
middle_item = list[2]
last_index = len(list) - 1
last_item = list[last_index]

print(first_item)
print(middle_item)
print(last_item)
#============================================================================================================
mixed_data_types = ['lewis',22,6.1,'Taken','Sky plaza']

company = ['Facebook','Google','Microsoft','Apple','IBM','Orcale','Amazon']
print(company)
print('The amount of companies is:', len(company))
first_item = company[0]
print(first_item)
middle_index = (len(company) / 2) 
middle_item = company[int(middle_index)]
print(middle_item)
last_index = len(company) - 1
last_item = company[last_index]
print(last_item)
company.insert(0,'Steam')
company.insert(4, 'GitHub')
print(company)
string = "#".join(company)
print(string)
company = ['Facebook','Google','Microsoft','Apple','IBM','Orcale','Amazon']
print(company.count('Facebook'))
company.sort()
print(company)
company.reverse()
print(company)
company = ['Facebook','Google','Microsoft','Apple','IBM','Orcale','Amazon']
first_three = company[0:3]
print(first_three)
last_three = company[-3:]
print(last_three)

middle_index = len(company) / 2
middle_item = company[int(middle_index)]
print(middle_item)
del company[0]
last_index = len(company) - 1
del company[last_index]
del company[int(middle_index)]
print(company)
del company[0:]
print(company)
del company # this deletes the whole list


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
