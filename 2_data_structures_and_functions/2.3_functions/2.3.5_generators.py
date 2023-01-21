def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for num in even_range(0, 10):
    print(num)

def fib(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

for num in fib(10):
    print(num)
