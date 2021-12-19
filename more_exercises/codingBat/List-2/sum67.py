
"""
Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6 and
extending to the next 7 (every 6 will be followed by at least one 7).
Return 0 for no numbers.
(https://codingbat.com/prob/p108886 - question link)
"""


def sum67(nums):
    record, total = True, 0
    for n in nums:
        if n == 6:
            record = False
        if record:
            total += n
            continue
        if n == 7:
            record = True
    return total