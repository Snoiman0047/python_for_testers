
def close_far(a, b, c):
    """
    Given three ints, a b c, return True if one of b or c is "close"
    (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.
    (https://codingbat.com/python/Logic-2 - link to question)
    :param a: any int value.
    :param b: any int value.
    :param c: any int value.
    :return: boolean value.
    """
    cond1 = abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2
    cond2 = abs(a - c) <= 1 and abs(a - b) >= 2 and abs(c - b) >= 2
    return cond1 or cond2
