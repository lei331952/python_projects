'''
Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.
'''
from collections import Counter


def count_vowels(text):
    vowels = 'aeiou'
    char_counts = Counter(text.lower())

    return {v: char_counts[v] for v in vowels if v in char_counts}


print(count_vowels('The input text eiouEIOU'))
