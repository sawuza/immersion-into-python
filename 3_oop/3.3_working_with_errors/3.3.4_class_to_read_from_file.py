class FileReader:

    def __init__(self, path):
        self._path = path

    def read(self):
        try:
            with open(self._path, "r") as f:
                data = f.read()
        except FileNotFoundError:
            data = ""
        return data
