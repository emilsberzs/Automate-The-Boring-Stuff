#! python3
# phone_and_email.py - Finds all phone numbers and email addresses in a chunk of text (USA format)

import pyperclip, re

phone_regex= re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code(either 3 digits, OR three digits in parentheses), optional
    (\s|-|\.)           # separator, space, - or .
    \d{3}               # first 3 digits
    (\s|-|\.)           # separator, space, - or .
    \d{4}               # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension, optional
    )''', re.VERBOSE) #Triple quotes and re.VERBOSE allows us to write regex as multiline

email_regex = re.compile(r'''(
            [a-zA-z0-9]+ # username
            @                 # @symbol
            [a-zA-Z0-9]+    # domain name
            (\.[a-zA-Z]{2,4}) # .something, 2-4 chars long
              )''',re.VERBOSE)

#Find matches in clipboard text

text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
       phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found in clipboard')
    