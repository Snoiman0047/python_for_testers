
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
(https://codingbat.com/prob/p118366 - question link)
"""


def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result