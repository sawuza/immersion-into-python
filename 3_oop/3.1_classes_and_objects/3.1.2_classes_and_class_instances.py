# классы нужны для того чтобы объединить функционал связанный общей идеей в одну сущность
# isinstans - это функция, которая в ран тайме позволяет посмотреть удовлетворяет какой-то объект какому либо классу
print(isinstance(2, int))

# объявление класса
class Human:
    pass

# создание экземпляра класса
class Planet:
    pass

planet = Planet()
print(planet)

# экземпляры классов хэшируются и могут быть ключами словаря
solar_system = {}
for i in range(8):
    planet = Planet()
    solar_system[planet] = True

print(solar_system)

# инициализация класса
# __str__ - позволяет переопределить то как будет печататься объект
class Planet:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

earth = Planet('Earth')
print(earth.name)
print(earth)

# работа с атрибутами экзкмпляра
mars = Planet('Mars')
print(mars)
print(mars.name)
mars.name = 'Second Earth?'
print(mars)

# del - удаление атрибута
del mars.name
print(mars.name)
