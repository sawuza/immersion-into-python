# наследование классов нужно для изменения поведения класса и расширение функционала класса
class Pet:

    def __init__(self, name=None):
        self.name = name

class Dog(Pet):

    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f"{self.name} : waw"

dog = Dog("Шарик", "Доберман")
