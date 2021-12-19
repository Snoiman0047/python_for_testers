
def round_sum(a, b, c):
    """
    Round an int value up to the next multiple of 10 by the rules.
    (its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round
    down to the previous multiple of 10 if its rightmost digit is less than 5.)
    (https://codingbat.com/prob/p179960 - link to question)
    :param a: any int value.
    :param b: any int value.
    :param c: any int value.
    :return: sum of rounded values.
    """
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
    return num + (10 - num % 10)