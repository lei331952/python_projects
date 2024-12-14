'''
Spell a number in English, support postive integers, negative integers, zero, and floating point numbers
'''
# pip install inflect

import inflect

p = inflect.engine()

n = 0
while True:
    n_str = input('Enter a number(-1 to stop): ')
    if n_str == '-1':
        break
    if '.' in n_str:
        n = float(n_str)
    else:
        n = int(n_str)
    print(p.number_to_words(n))
