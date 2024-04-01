#Raw string, ignores escape characters
print(r'This is raw string \' \" \n')

#Multiline triple quotes '''  
#'''
print('''This
      is
      Multiline triple 
      quote''')

'''Multiline
Comment'''

#Indexing and slicing strings
spam = 'hello world'

print('\nspam: ')
print(spam)

print('\nspam[0]: ')
print(spam[0])

print('\nspam[-1]')
print(spam[-1])

print('\nspam[0:5]')
print(spam[0:5])

print('''\nham = spam[0:5]
print(ham)''')
ham = spam[0:5]
print(ham)

#In and not in
print("\n'world' in spam")
print('world' in spam)

print("\n'world' in ham")
print('world' in ham)

#String interpretation with %s
name = 'Al'
age = 100
print("\n'My name is %s and i am %s years old' %(name, age)")
print('My name is %s and i am %s years old' %(name, age))

#fstring
print("\nf'My name is {name} and i am {age} years old'")
print(f'My name is {name} and i am {age} years old')

#upper() and lower()
print('\nname.upper()')
print(name.upper())

print('\nname.lower()')
print(name.lower())

#isupper() and islower()
print('\nham.isupper()')
print(spam.isupper())

print('\nham.islower()')
print(spam.islower())

'''
Other string methods:
isalpha() - Only letters
isdecimal() - Only numbers
isalnum() - Letters + numbers
isspace() - only spaces, tabs and newlines
istitle() - word that begin with uppercase followed by lowercase
startswith('string') 
endswith('string')
'''

#''.join()
to_join = ['cats','bats','fats','mats']
print('\nto_join: ')
print(to_join)

print("\n', '.join(to_join)")
print(', '.join(to_join))

print("\n' and '.join(to_join)")
print(' and '.join(to_join))

#.split()
dam = "This is an text,\nIt is written over several lines\nEach line is on a new line"

print("\ndam.split('\\n)'")
ram = dam.split('\n')
print(ram)

#.partition('string') returns tuple of three strings:(before,seperator, after)
print("\nspam.partition('w')")
print(spam.partition('w'))

#.rjust() .ljust() .center()
print("\nspam.rjust(20)")
print(spam.rjust(20))

print("\nspam.ljust(25,'*')")
print(spam.ljust(25,'*'))

print("\nspam.center(35, '=')")
print(spam.center(35, '='))

#.strip() .lstrip() .rstrip()
mam = '                  SpamSpamBaconSpamEggsSpamSpam                 '
print('\nmam=' + mam)

print("\nmam.lstrip()")
print(mam.lstrip())

print(mam.strip())

print("\ntam = mam.strip()")
tam = mam.strip()

print("\n(tam.strip('Samp')")
print(tam.strip('Samp'))

#ord() and char() 
print("\nord('a')") 
print(ord('a')) #returns Unicode code point

print("\nchr(100)")
print(chr(100)) #returns char at Unicode code point