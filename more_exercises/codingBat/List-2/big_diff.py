
"""
Given an array length 1 or more of ints,
return the difference between the largest and smallest values in the array.
return the smaller or larger of two values.
(https://codingbat.com/prob/p184853 - question link)
"""


def big_diff(nums):
    return max(nums) - min(nums)