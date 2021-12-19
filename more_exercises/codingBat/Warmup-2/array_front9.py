
"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.
(https://codingbat.com/prob/p110166 - question link)
"""


def array_front9(nums):
    return 9 in nums[:4]