# функция - это блок кода, которую можно использовать нсколько раз в разных местах программы
from datetime import datetime

def get_seconds():
    """Return current seconds"""
    return datetime.now().second

print(get_seconds())

# __doc__ - получить информационную строку
print(get_seconds.__doc__)

# __name__ - получить имя функции
print(get_seconds.__name__)

# функция с параметрами
def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())

    return tag_list

print(split_tags('python, course, stepik'))

# аннотация типов
def add(x: int, y: int) -> int:
    return x + y

print(add(10, 20))

# именованные аргументы
def say(name, greating):
    print('{} {}!'.format(greating, name))

say('Kitty', 'Hello')
say(greating='Hello', name='Kitty')
