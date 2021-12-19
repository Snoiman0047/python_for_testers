"""
Compute the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
Compute the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the above way.
(https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-59.php - question link)
"""

import math


def calc_sum_of_diagonals_numbers_on_spiral_by_formed(_formed_num):
    return math.ceil(((_formed_num * (_formed_num * (4 * _formed_num + 3) + 8) - 9) / 6))


formed_num = 5
print(f'sum of diagonals numbers on spiral {formed_num} by {formed_num} formed:',
      calc_sum_of_diagonals_numbers_on_spiral_by_formed(formed_num))
formed_num = 1001
print(f'sum of diagonals numbers on spiral {formed_num} by {formed_num} formed:',
      calc_sum_of_diagonals_numbers_on_spiral_by_formed(formed_num))

