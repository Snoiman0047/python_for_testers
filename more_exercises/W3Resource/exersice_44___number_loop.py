"""
Python program to construct the following pattern, using a nested loop number
(https://www.w3resource.com/python-exercises/python-conditional-exercise-44.php - question link)
"""


def print_number_loop(_num):
    print(f'{_num} loop:\n- - - - - -')
    [print(str(_num) * _num) for _num in range(1, _num + 1)]
    print('- - - - - -')


print_number_loop(int(input('please insert any number: ')))
