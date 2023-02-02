try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)

# доступ к объекту исключения, атрибут args
import os.path

file_name = "/file/not/found"
try:
    if not os.path.exists(file_name):
        raise ValueError("Файл не существует", file_name)
except ValueError or err:
    message, file_name = err.args[0], err.args[1]
    print(message, code)

# доступ  к стеку вызовов
import traceback

try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError or err:
    trace = traceback.print_exc()
    print(trace)

# генерация исключения, инструкция raise
try:
    raw = input("Введите число: ")
    if not raw.isdigit():
        raise ValueError
except ValueError:
    print("Некорректное значение!")

# исключение через raise from Exception
try:
    raw = input("Введите число: ")
    if not raw.isdigit():
        raise ValueError("Плохое число", raw)
except ValueError or err:
    print("Ошибка:", err.args[0], err.args[1])

    raise TypeError("Ошибка") from err

# иструкция assert
assert 1 == 0, "1 не равен 0"


# инструкция assert флаг -O (python3 -O namefile.py)
def get_user_by_id(my_id):
    assert isinstance(my_id, int), "id должен быть целым числом"

    print("Выполняем поиск")


if __name__ == "__main__":
    get_user_by_id("foo")
