
"""
Return the number of even ints in the given array.
(https://codingbat.com/prob/p189616 - question link)
"""


def count_evens(nums):
    return sum(1 for n in nums if n % 2 == 0)