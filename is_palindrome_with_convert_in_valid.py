def convert(w):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    f_p = ''
    for l in w:
        if l.lower() in alphabet:
            f_p += l
    return f_p

# print(convert('qwe, rty.. rrws sddsxf knwkjcb hbikuefhkfd'))


def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

word = 'nokek'

print(palindrome(convert(word)))
