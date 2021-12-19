
def no_teen_sum(a, b, c):
    """
    Calculate the amount of value other than those in the teen range. (13 - 19 excluding 15 - 16)
    (https://codingbat.com/prob/p100347 - link to question)
    :param a: any int value.
    :param b: any int value.
    :param c: any int value.
    :return: value fixed for the teen rule.
    """

    nums = (a, b, c)
    return sum(fix_teen(num) for num in nums)


def fix_teen(num):
    """
    Checking if the num is standing in the teen range. (13 - 19 excluding 15 - 16)
    :param num: any int value.
    :return: num param if he is standing in the teen rules otherwise return 0.
    """
    return 0 if num not in (15, 16) and 13 <= num <= 19 else num
