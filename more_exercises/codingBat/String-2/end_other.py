
"""
Given two strings, return True if either of the strings appears
at the very end of the other string, ignoring upper/lower case differences
(in other words, the computation should not be "case sensitive").
(https://codingbat.com/prob/p174314 - question link)
"""


def end_other(a, b):
    a, b = a.lower(), b.lower()
    return b.endswith(a) or a.endswith(b)