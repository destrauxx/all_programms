phrase = 'Fair is foul, and foul is fair: Hover through the fog and filthy air.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower_letters = 0
upper_letters = 0

print(phrase)

def lower_case(p):
    '''
    input: p - phrase(str)
    output: tmp, count of lower letters in p
    '''
    tmp = 0
    for i in p:
        for a in alphabet:
            if i == a.lower():
                tmp += 1
    return tmp

def upper_case(p, u):
    '''
    input - p - phrase(str), u - upper_letters(int)
    output - how in phrase upper letters
    '''
    tmp = 0
    for i in p:
        for a in alphabet:
            if i == a.upper():
                tmp += 1
    return tmp

lower_letters = lower_case(phrase)
upper_letters = upper_case(phrase, upper_letters)

print(f'Total lowercase letters in sentence is: {lower_letters}')
print(f'Total uppercase letters in sentence is: {upper_letters}')