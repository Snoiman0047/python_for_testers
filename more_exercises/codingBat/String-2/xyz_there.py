
"""
Return True if the given string contains an appearance of "xyz"
where the xyz is not directly preceded by a period (.).
(https://codingbat.com/prob/p149391 - question link)
"""


def xyz_there(str):
    return str.count('.xyz') != str.count('xyz')