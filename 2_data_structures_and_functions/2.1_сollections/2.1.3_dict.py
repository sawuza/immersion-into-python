# словари помогают хранить данные в формате (ключ:значение), и возможность получить значение по ключу за константное время
empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}
print(collections_map['mutable'])

# .get - возвращает указанное значение, если ключ в словаре не найден
print(collections_map.get('irresistible', 'not found'))

# in - проверяет содержится ли ключ в словаре
print('mutable' in collections_map)

# добавление элемента в словарь
beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar'
}
print(beatles_map)

beatles_map['Ringo'] = 'Drums'
print(beatles_map)

# удаление элемента из словаря
del beatles_map['John']
print(beatles_map)

# добавление при помощи метода (update)
beatles_map.update({
    'John': 'Guitar'
})
print(beatles_map)

# setdefault - проверяет на наличие ключа и добавляет его если не находит
unknown_dict = {}
print(unknown_dict.setdefault('key', 'default'))

# итерация по ключу словаря
print(collections_map)

for key in collections_map:
    print(key)

# итерация по ключу и значению
for key, value in collections_map.items():
    print('{} - {}'.format(key, value))

# итерация по значению словаря
for value in collections_map.values():
    print(value)

# OrderedDict из модуля collectoins - гарантирует что все ключи находятся в том порядке, в котором их туда добавили
from collections import OrderedDict

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)

for key in ordered:
    print(key)
