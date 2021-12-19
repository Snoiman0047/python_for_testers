import math


def reverse_string(_str):
    """
    Reverse the string sent as a parameter.
    :param _str:
    :return: reversed string.
    """
    reverse_str = ''
    index = len(_str) - 1
    while index >= 0:
        reverse_str += _str[index]
        index -= 1
    return reverse_str


def find_max_number(_num1, _num2, _num3):
    """
    Find the largest number of the three numbers sent as a parameter.
    :param _num1:
    :param _num2:
    :param _num3:
    :return: maximum number
    """
    return max(_num1, max(_num2, _num3))


def get_unique_list(original_list):
    """
    list without duplicates.
    :param original_list:
    :return: new list
    """
    new_list = []
    for element in original_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def factorial(_num):
    """
    Calculation of the factorial number sent as a parameter.
    :param _num:
    :return: sun of number factorial
    """
    if _num < 2:
        return 1
    else:
        return _num * factorial(_num - 1)


# exe 1

string = '1234-abcd'
print(f'string ({string}) after reversing:  {reverse_string(string)}')
print('\n')


# exe 2
num1, num2, num3 = 0, -9, 5
print(f'largest number ({num1},{num2},{num3}):  {find_max_number(num1, num2, num3)}')
print('\n')


# exe 3

num_list = [1, 2, 3, 3, 3, 3, 4, 5, 5]
print('unique list:', get_unique_list(num_list))
print('\n')


# exe 4

num = int(input('please insert any numbers: '))
print(f'factorial of {num}: {factorial(num)}')
print(f'factorial of {num} (build-in function): {math.factorial(num)}')

