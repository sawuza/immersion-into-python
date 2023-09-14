# создание процесса на Python
import time
import os
pid = os.fork()
if pid == 0:
    # дочерний процесс
    while True:
        print("child:", os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    print("parent:", os.getpid())
    os.wait()

# память родительского и дочернего процесса
foo = "bar"
if os.fork() == 0:
    # дочерний процесс
    foo = "baz"
    print("child:", foo)
else:
    # родительский процесс
    print("parent:", foo)
    os.wait()

# файлы в родительском и дочернем процессе
# cat data.txt
# example string1
# example string2
f = open("data.txt")
foo = f.readline()
if os.fork() == 0:
    # дочерний процесс
    foo = f.readline()
    print("child:", foo)
else:
    # родительский процесс
    foo = f.readline()
    print("parent:", foo)

# создание процесса, модуль multiprocessing
from multiprocessing import Process


def f(name):
    print("hello", name)


p = Process(target=f, args=("Bob",))
p.start()
p.join()

# создание процесса, модуль multiprocessing
from multiprocessing import Process


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


p = PrintProcess("Mike")
p.start()
p.join()
