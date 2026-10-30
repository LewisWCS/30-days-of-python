  # syntax
# while condition:
    # code goes here
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
# a while statement with an else
 # syntax
#while condition:
    #code goes here
#else:
    #code goes here
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#a while statment that breaks 
# syntax
#while condition:
    #code goes here
    #if another_condition:
        #break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# a continue while loop ususally used to skip variables
  # syntax
#while condition:
    #code goes here
    #if another_condition:
        #continue
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
  