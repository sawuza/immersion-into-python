import os
import tempfile


class File:
    def __init__(self, filename):
        self._filename = filename
        self._counter = 0
        open(self._filename, 'a+').close()

    def __str__(self):
        return self._filename

    def read(self):
        with open(self._filename, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self._filename, 'w') as f:
            return f.write(text)

    def __add__(self, obj):
        new_filename = os.path.join(tempfile.NamedTemporaryFile().name)

        file1 = self.read()
        file2 = obj.read()

        with open(new_filename, 'w+') as f:
            f.write(file1 + file2)

        return File(new_filename)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self._filename, 'r') as f:
            lines = f.readlines()

        if self._counter >= len(lines):
            self._counter = 0
            raise StopIteration

        line = lines[self._counter]
        self._counter += 1
        return line
