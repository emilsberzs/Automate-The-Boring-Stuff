'''Problems with pyperclip module, can't seem to get it to work one the current machine'''

#! python3
# multi_clipboard.py- Application for multi use clipboard

TEXT = {'agree':'I completely agree',
        'busy':'Sorry, im currently busy',
        'upsell':'Would You like anything else?'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py multi_clipboard.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)