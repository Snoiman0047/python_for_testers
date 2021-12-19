
def lucky_sum(a, b, c):
    """
    Calc sum of int values (a b c).
    However, if one of the values is 13 then it does not count towards the sum and
    values to its right do not count.
    (https://codingbat.com/prob/p107863 - link to question)
    :param a: any int value.
    :param b: any int value.
    :param c: any int value.
    :return: sum of int values.
    """

    total = 0
    for n in (a, b, c):
        if n != 13:
            total += n
        else:
            break
    return total
