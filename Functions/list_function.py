catNames = []
while True:
    print('Enter name to add to list: (Enter nothing to stop) ')
    name = input()
    if name == '':
        break
    catNames += [name]
print('The cat names are: ')
for name in catNames:
    print(name)

