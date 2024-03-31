def CommaCode(list):
    newString = ''
    if len(list) == 0:
        newString = 'No values in list'
    else:
        for word in list:
            if len(list) == 1:
                newString = newString + list[0] + '.'
            elif list.index(word) == len(list) -2:
                newString = newString + word + ' '
            elif list.index(word) != len(list) - 1:
                newString = newString + word + ', '
            else:
                newString = newString + 'and ' + word + '.'
    return newString



def comma_code(word_list):
    if not word_list:
        return 'No values in list'
    elif len(word_list) == 1:
        return word_list[0]
    else:
        return ', '.join(word_list[:-2]) + ', and ' + word_list[-1] + '.'
    
words = ['cat', 'bat', 'mat','spat']


print(comma_code(words))
print(CommaCode(words))