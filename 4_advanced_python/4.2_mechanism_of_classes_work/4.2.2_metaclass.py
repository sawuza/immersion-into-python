# мета классы
def dummy_factory():
    class Class:
        pass

    return Class


Dummy = dummy_factory()
print(Dummy() is Dummy())


# чтобы класс был мета, он должен насделоваться от другого мета-класса
class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass


# абстрактные методы
from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do something"""


class Child(Sender):
    def send(self):
        print('Sending')


print(Child())
