class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

earth = Planet('Earth')
mars = Planet('Mars')
print(Planet.count)
print(mars.count)

# деструктор экзкмпляра класса - когда счетчик ссылок на экз. класса достигает нуля, вызывается метод del

class Human:
    def __del__(self):
        print('Goodbye!')

human = Human()
del human

# словарь экземпляра и класса
class Planet:
    """This class describes planets"""

    count = 1

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

planet = Planet("Mars")
planet.mass = 5.97e24
print(planet.mass)
print(planet.__dict__)

# конструктор экз. класса - позволяет переопределить какие-то действия до его инициализации

class Planet:
    def __new__(cls, *args, **kwargs):
        print("__new__called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__called")
        self.name = name
