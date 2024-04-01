import pyperclip
spam = 'Hello world'
pyperclip.copy(spam)

ham= pyperclip.paste()

print(ham)