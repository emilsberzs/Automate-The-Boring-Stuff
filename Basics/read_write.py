'''Reading from file'''

text_file = open('C:\\Users\\Emils\\Desktop\\Uni\\AutomateTheBoringStuff\\Basics\\hello.txt') #Assign text file to variable
text_file_content = text_file.read() #Read contents of file into variable, puts whole contents of file into a single string
print('\n.read(): ')
print(text_file_content)
text_file.close() #Needs to be closed, otherwise its locked for access

text_file = open('C:\\Users\\Emils\\Desktop\\Uni\\AutomateTheBoringStuff\\Basics\\hello.txt') #Assign text file to variable
text_file_lines = text_file.readlines()
print('\n.readlines():')
print(text_file_lines)
text_file.close()

text_file = open('C:\\Users\\Emils\\Desktop\\Uni\\AutomateTheBoringStuff\\Basics\\hello.txt') #Assign text file to variable
text_file_first_line = text_file.readline() #Read first line
print('\ntext_file_first_line:')
print(text_file_first_line)
text_file.close()

'''Writing to file'''

write_file = open('text_file.txt', 'w') #Opens or creates blank text file in write mode
write_file.write('This was written through script\n') #Writes to file
write_file.close() #Close the file before opening again
write_file = open('text_file.txt', 'a') #Opens or creates file in append mode
write_file.write('And this was appended through script') #Appends another line
write_file.close() #Closes the file up
write_file = open('text_file.txt') #OPens in read mode
content = write_file.read() #Assigns whole text file to variable
write_file.close() #close up the file
print(content) #Prints it out


'''Saving variables using Shelve module'''

import shelve

shelf_file = shelve.open('my_data') #Creates new shelf files (.bak, .dat and .dir)
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats #Assigns variable to shelf file
shelf_file.close()

shelf_file = shelve.open('my_data')
print('\nlist(shelf_file.keys(): ')
print(list(shelf_file.keys()))

print('\nlist(shelf_file.values()): ')
print(list(shelf_file.values()))

print('\nlist(shelf_file.items())')
print(list(shelf_file.items()))


'''Saving variables with the pprint.pformat()'''

import pprint
cats = [{'name':'Zophie','description':'Chubby' }, {'name':'Pooka', 'description':'fluffy'}]
print('\npprint.pformat(cats): ')
print(pprint.pformat(cats))

file_object = open('my_cats.py', 'w')
file_object.write('cats = ' + pprint.pformat(cats) + '\n')
file_object.close()

import my_cats as my_cats

print('\nmy_cats.cats:')
print(my_cats.cats)