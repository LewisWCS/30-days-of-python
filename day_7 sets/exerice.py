# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
#5. remove() creates a ErrorKey message,discard() does not create ErrorKey
#join A and B
A.update(B)
print(A)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.intersection(B)
print(A)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('A is a subset of B:', A.issubset(B))
print('A and B are disjoint sets:', A.isdisjoint(B))
print(A.symmetric_difference(B)) # in a or b but not both so is like a xor gate
del A
del B
#Exercise 3 
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print('The list of age is bigger than the set of age:', len(age) > len(age_set))
print('The list of age is smaller than the set of age:', len(age) < len(age_set))
print('The list of age is equal the set of age:', len(age) == len(age_set))
#2 A string is a varible of list sets and tuples,list is a allowed duplicate unordered set of string
# A tuple is a list but cannot be edited 
# A set is a non allowed duplicate list of varibles
sentance = 'I am a teacher and I love to inspire and teach people'
sentance_words = sentance.split()
sentance_words = set(sentance_words)
print(sentance_words)
