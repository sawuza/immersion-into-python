# списки (list) - упорядоченный набор элементов, которые могут быть разных типов
empty_list = []
empty_list = list()

# len - узнать длинну списка
collections = ['int', 'float', 'dict']
len(collections)

# индексы
print(collections[0])

# замена элемента внутри списка при помощи индексов
collections[2] ='tuple'
print(collections)

# срезы (при срезе создается новый объект)
range_list = list(range(1, 10))
print(range_list)
print(range_list[1:3])
print(range_list[3:])

# итерация по элементам списка
collections = ['int', 'float', 'dict']

for collection in collections:
    print('Learning {} ...'.format(collection))

# enumerate - возвращает индекс и текущий элемент
for idx, collection in enumerate(collections):
    print("#{}  {}".format(idx, collection))

# append - добавление элемента списка
collections.append('OrderedDict')
print(collections)

# extend - дополнение списка другим списков(ex
collections.extend(['ponset', 'unicorndict'])
print(collections)

# + - так же добавляет элемент
collections += [None]
print(collections)

# del - удаляет элемент по индексу
del collections[4]
print(collections)

# min, max, sum
number = list(range(10))
print(min(number))
print(max(number))
print(sum(number))

# str.join - позволяет форматировать строку
tag_list = ["python", "course", "stepik"]
print(', '.join(tag_list))

# sorted - сортировка списка
import random

number = []
for _ in range(10):
    number.append(random.randint(1, 20))

print(number)
print(sorted(number))

number.sort(reverse=True)
print(number)
