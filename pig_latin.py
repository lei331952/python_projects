'''
Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is transposed 
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 
Read Wikipedia for more information on rules.
'''


def pig_latin(phrase):
    vowels = 'aeiouAEIOU'
    for i, letter in enumerate(phrase):
        if not letter in vowels:
            before, delimiter, after = phrase.partition(letter)
            return before + after + '-' + letter + 'ay'
    return phrase


print(pig_latin('banana'))
