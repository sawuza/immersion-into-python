# что бы определить дескриптор, нужно определить класс и задать у него методы __set__, __get__ или __delete__
class Descriptor:
    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')


class Class:
    attr = Descriptor()


instance = Class()
instance.attr = 10
del instance.attr


# пример
class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class Class:
    attr = Value()


instance = Class()
instance.attr = 10
print(instance.attr)


# дескриптор, который пишет в файл все присваиваемые ему значения
class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:
            f.write(str(value))

        self.amount = value


class Account:
    amount = ImportantValue(100)


bobs_account = Account()
bobs_account.amount = 150

with open('log.txt', 'r') as f:
    print(f.read())


# функции и методы (функции и методы реализованы с помощью дескрипторв)
class Class:
    def method(self):
        pass


obj = Class()
print(obj.method)
print(Class.method)


# собственный класс property
class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        return self.getter(obj)
