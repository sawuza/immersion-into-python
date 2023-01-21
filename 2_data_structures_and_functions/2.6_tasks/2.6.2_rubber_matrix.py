def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное None).
    :param size: int
    :return: list
    """
    matrix = list()
    for i in range(0, size):
        matrix.append([])
        for _ in range(0, size):
            matrix[i].append(None)
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

                # получаем размер матрицы
                matrix_size = len(matrix)

                # преобразуем матрицу в list
                matrix_list = list()
                for a in range(0, len(matrix)):
                    for b in range(0, len(matrix)):
                        matrix_list.append(matrix[a][b])

                # добавляем новые элементы в list
                for a in range(0, matrix_size * 2 + 1):
                    matrix_list.append(None)

                # делим на равные фрагменты
                new_matrix = list()
                for a in range(0, len(matrix_list), matrix_size + 1):
                    new_matrix.append(matrix_list[a:a + matrix_size + 1])

                return new_matrix

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
