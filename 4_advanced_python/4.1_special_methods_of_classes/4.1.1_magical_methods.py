# магический метод - это метод, который определен внутри класса, он начинается и заканчивается
# с двух подчеркиваний ( к примеру:__init__)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }


jane = User('Jane Doe', 'janedoe@example.py')
print(jane.get_email_data())


# метод __new__ отвечает за то, что происходит в момент создания объекта класса
class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


a = Singleton()
b = Singleton()
print(a is b)


# __str__ определяет поведение при вызове функции
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)


jane = User('Jane Doe', 'janedoe@example.py')
print(jane)


# __hash__, __eq__ определяют то, как сравниваются  объекты и что происходит при вызове функции hash
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email


jane = User('Jane Doe', 'jdoe@example.py')
joe = User('Joe Doe', 'jdoe@example.py')
print(jane == joe)
print(hash(jane))
print(hash(joe))


# __getattr__, __getattribute__, __setattr__, __delattr__ - методы, определяющие доступ к аттрибутам
# __getarrt__  - определяет поведение, когда атрибут не найден
class Researcher1:
    def __getattr__(self, name):
        return 'Nothing found: \n'

    def __getattribute__(self, name):
        print('Looking for {}'.format(name))
        return object.__getattribute__(self, name)


obj1 = Researcher1()
print(obj1.attr)
print(obj1.method)
print(obj1.DFG2)


# __getattribute__ - вызывается в любом случае
class Researcher:
    def __getattr__(self, name):
        return 'Nothing found'

    def __getattribute__(self, name):
        return 'nope'


obj = Researcher()
print(obj.attr)
print(obj.method)
print(obj.DFG2)


# __setatrr__ определяет поведение при присваивании значения к атрибуту
class Ignorant:
    def __setattr__(self, name, value):
        print('Not gonna set {}!'.format(name))


obj = Ignorant()
obj.math = True


# __delattr__  управляет поведением, когда пытаемся удалить атрибут объекта
class Polite:
    def __delattr__(self, name):
        value = getattr(self, name)
        print(f'Goodbye {name}, you were {value}!')

        object.__delattr__(self, name)


obj = Polite()
obj.attr = 10
del obj.attr


# __call__ определяет поведение, когда вызывается класс
def __call__(self, func):
    def wrapped(*args, **kwargs):
        with open(self.filename, 'a') as f:
            f.write('Oh Danny boy...')

        return func(*args, *kwargs)

    return wrapped


# __add__ перегружает операцию сложения
import random


class NoisyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        noise = random.uniform(-1, 1)
        return self.value + other.value + noise


a = NoisyInt(10)
b = NoisyInt(20)
