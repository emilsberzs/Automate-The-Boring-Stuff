foo = {
    'name':'paws', 
    'species':'cat', 
    'color':'gray'
    }

bar = {
    'species':'cat',
    'color':'gray',
     'name':'paws'    
        }

#Order doesn't matter
print('\nFoo == Bar')
print(foo == bar)

#Print values
print('\nValues:')
for v in foo.values():
    print(v)

#Print keys
print('\nKeys:')
for k in foo.keys():
    print(k)

#Print both, keys and values:
print('\nKey Value:')
for k, v in foo.items():
    print('Key: ' + k + ' Value: ' + v)

#OR
print('\nItems')
for i in foo.items():
    print(i)

#Values as list
print('\nValues as list: ')
print(list(foo.values()))

#Keys as list
print('\nKeys as list:')
print(list(foo.keys()))

#Items as list
print('\nItems as list:')
print(list(foo.items()))
    
#Check if value or key in dictionary
print('\nCheck if key in dict: ')
print('Is "name" in foo? : ')
print('name' in foo.keys())

print('\nCheck if value in dict: ')
print('Is "paws" in foo? : ')
print('paws' in foo.values())
