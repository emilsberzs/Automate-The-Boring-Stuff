#!python3
# mclip.py - A multi clipboard program

TEXT = {'agree':"""Yes I agree, that sounds fine""",
        'busy':"""I'm busy at the moment, i'll get back to You later""",
        'upsell':"""Would You consider doing this on a monthly basis?"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclpip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
