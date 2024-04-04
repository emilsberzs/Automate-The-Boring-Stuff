import re
message = 'Call me at 415-555-1011. My work number is 111-222-3333'


phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # create regex object with re.compile() always use raw string (r'string')
mo = phone_num_regex.search(message) # mo-match object. pass the string to be searched by regex objects .search method

print('Phone number found: ' + mo.group())  



'''Grouping with parentheses'''

another_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #Puts first three digits in separate group
match_object = another_num_regex.search(message)

print(match_object.groups()) #groups() gets all groups
print(match_object.group()) #gets all matched text
print(match_object.group(0)) #same as group()
print(match_object.group(1)) #First group
print(match_object.group(2)) #second group
area_code,main_number = match_object.groups() #Use multiple assignment trick, assign each group to separate variable
print('Area code: ' + area_code + ' , ' + 'Main number: ' + main_number + '.')
print(phone_num_regex.findall(message)) #findall() finds all instances of specified string


'''| Matching multiple objects with a pipe |'''

bat_string = 'Batmobile lost a wheel'
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
bat_match_object = bat_regex.search(bat_string)

print(bat_match_object.group())
print(bat_match_object.group(1))


'''More regex features

(string)? - Optional matching
(string)* - Zero or more
(string)+ - One or more
(string){3} -Must be three times
(string){3,5} -Three , four or five, will return maximum number, greedy.
(string){3,5}? -Three , four or five, will return minimum number, lazy.
(string){3,} -Atleast 3 times
(string){,5} -Up to 5 times


Shorthands
\d - digits 0-9
\D - any char NOT a digit 0-9
\w - any digit, letter, underscore
\W - any NOT a digit, letter, underscore
\s - any space, tab, newline
\S - any NOT space, tab, newline
^string - starts with string
string$ - ends with string
. - any character
.*? - any amount of any characters, lazy
.* -any amount of any character greedy
[abc] - any character between braces
[^abc] - any character not between braces


Making Your own classes:

vowel_regex = re.compile(r'[aeiouAEIOU]')
alpha_numeric_regex = re.compile(r'[a-zA-Z0-9])
vowel_regex.findall('some string')
'''



#Substituting strings with sub() method

names_regex = re.compile(r'Agent \w+')
censored_string = names_regex.sub('CENSORED','Agent Alice gave documents to Agent Bob')
print(censored_string)

agent_names_regex = re.compile(r'Agent (\w)\w*') #This is juts to make 2 different groups, one for first char,  second for remainder of a string
encrypted_message = agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew that Agent Bob was a double agent')
print(encrypted_message)


#Managing complex Regexes on multilines

phone_regex= re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code(either 3 digits, OR three digits in parentheses)
    (\s|-|\.)           #separator, space, - or .
    \d{3}               #first 3 digits
    (\s|-|\.)           #separator, space, - or .
    \d{4}               #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  #extension
    )''', re.VERBOSE) #Triple quotes and re.VERBOSE allows us to write regex as multiline


#Combining re.IGNORECASE ,re.DOTALL and re.VERBOSE
some_regex = re.compile(r'foo', re.IGNORECASE | re.DOTALL, re.VERBOSE)