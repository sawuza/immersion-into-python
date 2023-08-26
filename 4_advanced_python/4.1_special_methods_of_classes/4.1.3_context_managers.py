# __enter__, __exit__ отпределяют что происходит в начале и конце контекстного менеджера
class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


# контекстный менеджер, который считает время проведенное в нем
import time

class timer():
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('Elapsed: {}'.format(self.current_time))


with timer() as t:
    time.sleep(1)
    t.current_time()
    time.sleep(1)
