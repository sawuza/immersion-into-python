# в функции можно передавать другие функции
def caller(func, params):
    return func(*params)

def printer(name, origin):
    print('I\'m {} of {}'.format(name, origin))

caller(printer, (['Moana', 'Motunui']))

# функция в функции
def get_multipier():
    def inner(a, b):
        return a * b
    return inner

multiplier = get_multipier()
print(multiplier(10, 11))

# функция map()
def squarify(a):
    return a ** 2

print(list(map(squarify, range(10))))

# функция filter
def is_positive(a):
    return a > 0

print(list(filter(is_positive, range(-5,5))))

# анонимная функция lambda
print(list(map(lambda x: x ** 2, range(5))))

def swap(num_list):
    return list(map(str, num_list))

print(swap(range(10)))

# модуль functools
from functools import reduce

def multiply(a, b):
    return a * b

print(reduce(multiply, [1, 2, 3, 4, 5]))

# списочные выражения
square_list = [number ** 2 for number in range(10)]
print(square_list)

# функция zip  позволяет склеить два итерабельных объекта
num_list = range(7)
squared_list = [x ** 2 for x in num_list]

print(list(zip(num_list, squared_list)))
