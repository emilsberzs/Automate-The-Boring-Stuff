#Counts how many times each character repeats in a string
import pprint
message = 'It was bright cold day in April, and the clocks were striking thirteen hours x.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

pprint.pprint(count)