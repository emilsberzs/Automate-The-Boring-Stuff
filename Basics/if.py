print('Name: ')
name = input()
print('Password : ')
password = input()
if name == 'Mary' :
    print('Hello Mary')
    if password == 'secret':
        print('Access granted.')
    else:
        print('Access denied.')