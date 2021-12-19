
def lone_sum(a, b, c):
    """
    Calculate the sum of the 3 values without identical values.
    (https://codingbat.com/prob/p143951 - link to question)
    :param a: any int value.
    :param b: any int value.
    :param c: any int value.
    :return: sum of the values.
    """

    nums = (a, b, c)
    return sum(n for n in nums if nums.count(n) == 1)
