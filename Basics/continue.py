while True:
    print('Who are You?')
    name = input()
    if name != 'Emils':
        continue
    print('Hello Emils, what is the password?')
    password = input()
    if password == 'secret':
        break
print('Access granted')