
"""
Given a string, return a string where for every char in the original, there are two chars.
(https://codingbat.com/prob/p170842 - question link)
"""


def double_char(str):
    return ''.join(char * 2 for char in str)