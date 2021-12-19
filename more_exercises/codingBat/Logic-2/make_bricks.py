
def make_bricks(small, big, goal):
    """
    Calculate the minimum number of bricks required to create a row of bricks with a target length of inches.
    (https://codingbat.com/prob/p118406 - link to question)
    :param small: The number of small bricks (1 inch) in stock.
    :param big: The number of large bricks (5 inch) in stock.
    :param goal: The desired weight of the chocolate package to be produced.
    :return: A Boolean value that expresses whether the goal can be done by choosing from the given bricks.
    """

    # Logic explanation:
    # Verification 1:
    # there are enough small bricks to reach the goal.
    # Verification 2:
    # there are large bricks enough than required and
    # enough small bricks to cover the remainder in case the non-dual purpose of 5.

    return small >= goal % 5 and small + 5 * big >= goal
