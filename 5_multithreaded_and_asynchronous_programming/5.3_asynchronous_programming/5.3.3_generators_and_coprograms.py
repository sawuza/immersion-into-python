# сопрограммы (корутины)
def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)

# сопрограммы, вызов метода close()
def grep(pattern):
    print("start grap")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")

# вызовы сопрограмм, PEP 380
def grep(pattern):
    print("start grap")
    while True:
        line = yield
        if pattern in line:
            print(line)

def grep_python_coroutine():
    g = grep("python")
    yield from g

g= grep_python_coroutine()
print(g)
g.send(None)
