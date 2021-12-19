
def make_chocolate(small, big, goal):
    """
    Calculate the number of small packs to use to make a chocolate package that weighs as goal.
    (https://codingbat.com/prob/p190859 - link to question)
    :param small: The number of small packs (1 kg) in stock.
    :param big: The number of large packs (5 kg) in stock.
    :param goal: The desired weight of the chocolate package to be produced.
    :return: the number of small bars to use.
    """

    # Logic explanation:
    # There are 2 ways to get the desired compound:

    # If we have more large decks than necessary and small decks are enough to cover the
    # rest in case and the non-dual goal of 5.
    if big >= (goal // 5) and small >= goal % 5:
        return goal % 5
    # If there are enough small decks to reach the goal after using all the large decks.
    if big <= (goal // 5) and small >= goal - big * 5:
        return goal - big * 5
    return -1
