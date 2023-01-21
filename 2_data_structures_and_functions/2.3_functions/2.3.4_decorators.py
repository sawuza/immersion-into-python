# декоратор - это функция, которая принимает функцию и возвращает функцию
def decorator(func):
    return func

@decorator
def decorated():
    print('Hello')

decorated = decorator(decorated)

# написать декоратор, который записывает в лог результат декорируемой функции
def logger(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

print(summator([1, 2, 3, 4, 5]))

with open('log.txt', 'r') as f:
    print('log.txt: {}'.format(f.read()))
