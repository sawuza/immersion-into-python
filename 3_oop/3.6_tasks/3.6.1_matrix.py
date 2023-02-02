class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        if max_size is not None:
            self.MAX_SIZE = max_size

        self._mtrx = [None]

    def append(self, element=None):
        if element is None:
            return self._mtrx

        try:
            idx = self._mtrx.index(None)
            if len(self._mtrx) ** 0.5 == self.MAX_SIZE:
                self._mtrx[idx] = element
            else:
                self._mtrx[idx] = element
                size = int(len(self._mtrx) ** 0.5)
                if idx == size * (size - 1):
                    self._mtrx.extend([None, ] * ((size + 1) ** 2 - len(self._mtrx)))
            return self._mtrx
        except Exception:
            raise IndexError

    def pop(self):
        if self._mtrx[0] is None:
            raise IndexError

        if len(self._mtrx) == 1:
            arg = self._mtrx[0]
            self._mtrx = [None]
            return arg
        else:
            element_x = int(((len(self._mtrx) ** 0.5 - 1) ** 2 - (len(self._mtrx) ** 0.5 - 2)))
            idx = self._mtrx.index(None, 0, len(self._mtrx))

            if idx == element_x:
                arg = self._mtrx[idx - 1]
                self._mtrx[idx - 1] = None
                self._mtrx = self._mtrx[0: int((len(self._mtrx) ** 0.5 - 1) ** 2)]
            else:
                arg = self._mtrx[idx - 1]
                self._mtrx[idx - 1] = None
            return arg

    def __str__(self):
        result = ''
        size = int(len(self._mtrx) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i) for i in self._mtrx[size * row:size * (row + 1)]]) + '\n'
        return result


    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        try:
            iter(iter_obj)
        except Exception:
            raise TypeError

        new_matrix = cls(max_size)
        for obj in iter_obj:
            if obj is not None:
                new_matrix.append(obj)
        return new_matrix

# matrix = Matrix()
# print(matrix)
# matrix.append(2)
# print(matrix)
# print('----------')
# print(matrix.pop())
# print('----------')
# print(matrix)
# matrix = Matrix.from_iter(range(9), max_size=4)
# print(matrix)
# matrix = Matrix.from_iter(''.join(str(s) for s in range(10)), max_size=3)
