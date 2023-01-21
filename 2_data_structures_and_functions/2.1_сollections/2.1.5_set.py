# множества позволяют хранить в неупорядоченном виде набор уникальных объектов
empty_set =  set()
number_set = {1, 2, 3, 3, 4, 5}
print(number_set)

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)
print(odd_set)
print(even_set)

# объединение двух множеств
union_set = odd_set |even_set
union_set = odd_set.union(even_set)

print(union_set)

# пересечение множеств
intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)

print(intersection_set)

# значение которые содержатся в одном множестве, но не содержатся в другом множестве
difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)

print(difference_set)

# удаление элемента из множества
even_set.remove(2)
print(even_set)
