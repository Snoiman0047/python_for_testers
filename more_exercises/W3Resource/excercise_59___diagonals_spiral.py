import math
import numpy as np
from pandas import *


def create_squared_matrix(random_range, size):
    _squared_matrix = np.random.randint(random_range + 1, size=(size, size))
    print(f'Squared matrix {np.shape(_squared_matrix)} was created!')
    return _squared_matrix


def print_squared_matrix(_squared_matrix):
    print('  *  ' * 3, '\n')
    print(DataFrame(_squared_matrix), '\n')
    print('  *  ' * 3, '\n')


def get_sum_of_squared_metrix_trace(_squared_matrix):
    return np.trace(_squared_matrix)


def get_squared_metrix_plip(_squared_matrix):
    return np.fliplr(_squared_matrix).diagonal()


def get_sum_of_squared_metrix_diagonals(_squared_matrix):
    metrix_flip = get_squared_metrix_plip(_squared_matrix)
    if len(metrix_flip) % 2 != 0:
        metrix_flip = np.delete(metrix_flip, math.ceil(len(metrix_flip) / 2))
    return sum(metrix_flip) + get_sum_of_squared_metrix_trace(_squared_matrix)


squared_matrix = create_squared_matrix(9, 5)
print('\n')
print_squared_matrix(squared_matrix)
print('Sum squared metrix diagonals:', get_sum_of_squared_metrix_diagonals(squared_matrix))