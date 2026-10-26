ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.insert(0,19)
last_index = len(ages)
ages.insert(last_index, 26)
print(ages)
middle_index = len(ages) / 2
median = ages[int(middle_index)]
print(median)
average = sum(ages) / len(ages)
print(average)
last_index = len(ages) - 1
ranges = ages[last_index] - ages[0]
print(ranges)

value_1 = abs(ages[0] - average)
value_2 = abs(ages[last_index] - average)

print(value_1)
print(value_2)