# обработка исключений
try:
    1/0
except:
    print("Ошибка")

while True:
    try:
        raw = input("Введите число: ")
        number = int(raw)
        break
    except ValueError:
        print("Некорректное значение")
    except KeyboardInterrupt:
        print("Выход")
        break


data_base = {
    "red": ["fox", "flower"],
    "green": ["peace", "M", "python"]
}

try:
    color = input("Введите цвет: ")
    number = input("Введите номер по порядку: ")

    label = data_base[color][int(number)]
    print("Вы выбрали: ", label)
#exept (IndexError, KeyError)
except LookupError:
    print("Объект не найден")

finally:
    print("Этот блок будет выполнен в любом случае")
