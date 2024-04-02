import re

message = 'Call me at 415-555-1011. 415-555-9999 is my Office'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # always use raw string (r'string')

mo = phoneNumRegex.search(message) # mo-match object

print('Phone number found: ' + mo.group())
