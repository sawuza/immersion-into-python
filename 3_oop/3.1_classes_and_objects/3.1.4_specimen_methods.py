# методы - это функции, которые действуют в контексте экземпляра класса
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f'Welcome to {self.name}, {human.name}!')
        self.population.append(human)

mars = Planet('Mars')
bob = Human('Bob')
mars.add_human(bob)

# вызов методов из методов
class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f'Hello, I am {self._name}')

    def say_how_old(self):
        self._say(f'I am {self._age} years old')

bob = Human('Bob', age=29)
bob.say_name()
bob.say_how_old()

# метод класса (@classmethod)
class Event:

    def __init__(self, discription, event_date):
        self.discription = discription
        self.date = event_date

    def __str__(self):
        return f'Event \"{self.discription}\" at {self.date}'

from datetime import date

event_discription = "Рассказать, что такое @classmethod"
event_date = date.today()

event = Event(event_discription, event_date)
print(event)



# добавим метод класса
def extract_description(user_string):
    return "открытие чемпионата мира по футболу"

def extarct_date(user_string):
    return date(2023, 1, 22)

class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f'Event \"{self.description}\" at {self.date}'

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extarct_date(user_input)
        return cls(description, date)

event = Event.from_string("Добавить в мой календарь открытие ЧМ по футболу  на 22 января 2023 года")
print(event)
