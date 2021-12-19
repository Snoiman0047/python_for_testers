"""
Python program to get days between two dates.
(https://www.w3resource.com/python-exercises/python-basic-exercise-14.php - question link)
"""

from datetime import datetime


def calc_days_between_days(date_1, date_2, date_format='%d.%m.%Y'):
    return int((datetime.strptime(date_1, date_format) - datetime.strptime(date_2, date_format)).days)


_date1 = input('please enter any date: ')
_date2 = input('please enter any date: ')
print(f'days between {_date1} to {_date2}', calc_days_between_days(_date1, _date2))

