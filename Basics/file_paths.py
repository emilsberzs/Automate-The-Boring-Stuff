from pathlib import Path
import os

my_files = ['birthdays.py', 'break.py', 'continue.py']
for filename in my_files:
    print(Path(r'C:\Users\emils\Desktop\AutomateTheBoringStuff\Basics', filename))


#Print Current Working Directory
print(Path.cwd())

#Change Current Working Directory
os.chdir(str(Path.cwd()) + '\Basics')
#OR
print(Path.cwd())
os.chdir('c:\\Users\\emils\\Desktop\\Uni\\AutomateTheBoringStuff\\Basics')
print(Path.cwd())

#Print Home Directory
print(Path.home())

'''Create folders'''
#os.makedirs(str(Path.cwd()) + '\\new\\folders')    #Creates all necessary sub folders
#Path(r'C:\\Users\\Emils\\Desktop\\Uni\\AutomateTheBoringStuff\\Basics\\Single_Folder').mkdir() #Will create only one folder, nu subfolders


#Absolute and relative paths
print(Path.cwd().is_absolute()) #Absolute
print(Path('/AutomateTheBoringStuff/').is_absolute()) #Relative

#Get absolute path from relative path
print(Path.cwd() / Path('my/relative/path'))

print(os.path.abspath('..\\Projects'))

#Getting attributes (parts) from file path:
p = Path('C:/Users/emils/Desktop/Uni/AutomateTheBoringStuff/Basics/read_write.py') #Assign path to variable
print('\np: ')
print(p)

print('\np.anchor:')
print(p.anchor) #Gets anchor (very base of path)

print('\np.name: ')
print(p.name) #Gets very top of path, including extension for file

print('\np.stem: ')
print(p.stem) #Gets very top of the path, excluding extension for file

print('\np.suffix :')
print(p.suffix) #gets extension for a file

print('\np.drive: ')
print(p.drive) #Gets drive name wjere the path originates (without \)

print('\np.parent: ')
print(p.parent) #Gets direct parent of filepath target

print('\np.parents[0]: ')
print(p.parents[0]) #Direct parent

print('\np.parents[1]: ')
print(p.parents[1]) #Parent of parent

print('\np.parents[2]: ')
print(p.parents[2]) #Parent of parent of parent etc



#Find file size in bytes:
print('\nFilesize: ')
print(os.path.getsize(str(Path.cwd()) + '\\file_paths.py'))

#Find folder size in bytes:
total_size = 0
for filename in os.listdir(Path.cwd()):
    total_size = total_size + os.path.getsize(os.path.join(Path.cwd(), filename))
print('\nFolder size: ')
print(total_size)

#Modifying a list of files using Glob Patterns (kind of regexes)
p = Path('C:/Users/emils/Desktop/Uni/AutomateTheBoringStuff')
print("\np.glob('*')")
print(p.glob('*'))

print("\nlist(p.glob('*'))")
print(list(p.glob('*')))

print("\nlist(p.glob('*.py'))")
print(list(p.glob('*.py')))


#Check if path returns file or directory
print('\np.exists(): ')
print(p.exists())

print('\np.is_file(): ')
print(p.is_file())