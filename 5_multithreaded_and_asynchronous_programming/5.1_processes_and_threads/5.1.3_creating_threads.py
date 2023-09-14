# создание потока
from threading import Thread


def f(name):
    print("hello", name)


th = Thread(target=f, args=("Bob",))
th.start()
th.join()

# создание потока
from threading import Thread


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


th = PrintThread("Mike")
th.start()
th.join()

# пул потоков, concurrent.futures.Future
from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a

# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
