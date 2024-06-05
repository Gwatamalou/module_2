# Я бы делал вот так
"""
import numpy as np


def get_matrix(n, m, value):
    return np.tile(value, (n, m, 5, 4))


print(get_matrix(int(input('enter number of lines: ')), int(input('enter number of columns: ')),
                     input('enter value: ')))
"""

# Но по заданию вот так, ну очень не красиво
def get_matrix_2(n, m, value):
    matrix = []
    for i in range(0, n):
        i_matrix = []
        for j in range(0, m):
            i_matrix.append(value)
        matrix.append(i_matrix)
    return matrix


print(get_matrix_2(int(input('enter number of lines: ')), int(input('enter number of columns: ')),
                   input('enter value: ')))


# Если уже делать без нумпай то хтоябы так
"""
def get_matrix_3(n, m, value):
    matrix = [[value] * m for i in range(n)]
    return matrix


print(get_matrix_3(int(input('enter number of lines: ')), int(input('enter number of columns: ')),
                   input('enter value: ')))
"""
