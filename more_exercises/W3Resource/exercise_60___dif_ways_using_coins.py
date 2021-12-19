"""
Python program to find different ways where £2 be made using any number of coins.
(https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-62.php - question link)
"""


def calc_optional_ways(_array, _length, num):
    if num == 0:
        return 1
    if num < 0 or (_length <= 0 and num >= 1):
        return 0
    return calc_optional_ways(_array, _length - 1, num) + calc_optional_ways(_array, _length, num - _array[_length - 1])


coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(f'Found {calc_optional_ways(coins, len(coins), 200)} optional ways where £2 be made using any number of coins.')
