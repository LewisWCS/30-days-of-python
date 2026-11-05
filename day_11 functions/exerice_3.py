#num= int(input('Give me a interger n: '))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
# failed attempt
#def unique_items(*arg):
    #args = list(arg)
    #for items in args:
        #if args.count(items) > 1:
            #remo = len(items) - 1
            #print(items, 'is duplicated and will now be deleted')
            #args.remove(items)
        #else:
            #continue
    #print(args)

def unique_items(*arg):
    unique = []
    for items in arg:
        if items not in unique:
            unique.append(items)
        else:
            continue
    print(unique)
unique_items(1,3,4,5,3,2,2,2,3,4,5)




        
        
