
"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
(https://codingbat.com/prob/p182414 - question link)
"""


def string_match(a, b):
    shorter = min(len(a), len(b))
    return sum(1 for i in range(shorter-1) if a[i:i+2] == b[i:i+2])