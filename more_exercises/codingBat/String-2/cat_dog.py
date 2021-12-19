
"""
Return True if the string "cat" and "dog" appear
the same number of times in the given string.
(https://codingbat.com/prob/p164876 - question link)
"""


def cat_dog(str):
    return str.count('cat') == str.count('dog')