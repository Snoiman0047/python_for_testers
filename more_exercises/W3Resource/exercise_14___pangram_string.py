"""
Python function to check whether a string is a pangram or not.
(https://www.w3resource.com/python-exercises/python-functions-exercise-14.php - question link)
"""

import string


def is_pangram(_sentence, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(_sentence.lower())


sentence = input('please insert some sentence: ')
print(f'is {sentence} pangram:', is_pangram(sentence))