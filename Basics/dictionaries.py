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
#print(foo == bar)


birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
    print('Enter a name: (leave blank to quit)\n')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have information for ' + name)
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday added to database!')
