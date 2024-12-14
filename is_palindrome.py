'''
Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar"
'''


def is_palindrome(s):
    s_clean = s.replace(' ', '')
    return s_clean == s_clean[::-1]


def is_palindrome2(s):
    s_clean = s.replace(' ', '')
    left, right = 0, len(s_clean) - 1

    while (left < right):
        if (s_clean[left] != s[right]):
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome2('racecar'))
print(is_palindrome2('this'))
