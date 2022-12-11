
SPACE = 'sp'
BACK_SLASH = 'bS'
SINGLE_QUOTE = 'sQ'
NEW_LINE = 'nl'

specials = {
    SPACE: ' ',
    BACK_SLASH: '\\',
    SINGLE_QUOTE: '\'',
    NEW_LINE: '\n'
}

#raw = input()
raw = '1sp 1/ 1bS 1_ 1/ 1bS nl 1( 1sp 1o 1. 1o 1sp 1) nl 1sp 1> 1sp 1^ 1sp 1< nl 2sp 3|'
formatted = ''

for chunk in raw.split():
    if chunk == NEW_LINE: formatted += specials[NEW_LINE]
    else:
        char = ''
        multiplier = 0
        if chunk[-2:] in specials:
            multiplier = chunk[0:len(chunk) - 2]
            char = specials[chunk[-2:]]
        else:
            multiplier = chunk[0:len(chunk) - 1]
            char = chunk[-1:]
        formatted += char * int(multiplier)

print(formatted)
