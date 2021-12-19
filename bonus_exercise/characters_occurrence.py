def characters_occurrence(string):
    """
    Calculate the number of occurrences of each character in the string
    (without spaces and the difference between lowercase and uppercase letters).
    :param string:
    :return: set
    """
    string = _str.replace(' ', '')
    return sorted(({x: _str.count(x) for x in set(string)}).items())

# exe 1 (Print instances of a character in a word.)

_str = input('please insert something: ')
print(f"Occurrence of all characters in {_str} is :", (characters_occurrence(_str)))
print('\n')




