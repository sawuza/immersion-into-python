import numpy as np

def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное None).
    :param size: int
    :return: list
    """
    matrix = np.array([None, ] * (size ** 2)).reshape(size, size)
    return matrix

def add_element(element, matrix):
    """
    Функция добавляет element в матрицу matrix и при необходимости изменяет размер
    матрицы. Возвращает полученную матрицу.
    :param element: string
    :param matrix: list
    :return: list
    """
    if element is None:
        return matrix

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == len(matrix) - 1 and j == 0:
                matrix[i][j] = element
                matrix_len = len(matrix)
                matrix_list = matrix.flatten().tolist()
                matrix_add_list = np.array([None, ] * (matrix_len * 2 + 1))
                matrix_list = np.concatenate((matrix_list, matrix_add_list), axis=None)
                matrix = np.array(matrix_list).reshape(matrix_len + 1, matrix_len + 1)
                return matrix

            if matrix[i][j] is None:
                matrix[i][j] = element
                return matrix

def matrix_to_string(matrix):
    """
    Функция создает строковое представление matrix
    :param matrix: list
    :return: string
    """
    matrix_str = ''
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if j == len(matrix) - 1:
                matrix_str += str(matrix[i][j])
                matrix_str += '\n'
            else:
                matrix_str += str(matrix[i][j]) + ' '

    return matrix_str

m = create_matrix(2)
for i in range(13):
    m = add_element(i, m)
print(matrix_to_string(m))
