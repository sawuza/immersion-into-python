n = "Курс по \"Python\" на stepik "
print(n)

# сырые строки (r - строки)

# с помощью "\" экранируем спец. символ
m = "Файл на диске C:\\\\"
print(m)

# с помощью сырых строк(r) можно не экранировать спец. символ
v = r"Файл на диске C:\\"
print(v)

# при помощи "\" выполняем перенос строки на след. строку + соблюдаем табуляцию
example_str = "Курс по пайтон " \
            "это возможность быстро и легко " \
            "изучить язык программирования"
print(example_str)

obzats = """
Таким способом можно 
записывать строки 
состоящие из нескольких абзацев
"""
print(obzats)

# строки неизменяемые. Создается новый строковой объект в памяти
my_str = "Hello"
print(id(my_str))
my_str += ", world"
print(id(my_str))

# срезы строк [start:stop:step]
srez = "Python course"
print(srez[7::])
print(srez[::-1])


# метод count() позволяет найти кол-во вхождений символа
quote = "Болтовня ничего не стоит. Покажи мне код."
print(quote.count("о"))

# метод capitalize() делает первую букву в стоке заглавной
q = "москва"
print(q.capitalize())

# метод isdigit() проверяет является ли строка, числом
print("210".isdigit())

# оператор in проверяет наличие подстроки в строке
print("3.14" in "Число Пи = 3.1415926")

# оператор for.. in производит итерацию по строке
iter_str = "Hello"
for letter in iter_str:
    print("Буква:", letter)

# конвертация типов
# преобразуем число в строку класса str
konvert = str(912.33)
print(konvert, type(konvert))


# форматирование строк
# 1-ый способ "%s"

template = "%s - главное достоинство программиста. (%s)"
print(template % ("Лень", "Larry Wall"))

# 2-ой способ ".format()"
print("{} не лгут, но {} пользуются формулами".format("Цифры", "лжецы"))
print("{num} Кб должно хватать для любых задач. ({author})".format(num = 640, author = "Bill Gates"))

# f - строки
subject = "оптимизация"
aut = "Donald Knuth"

print(f"Преждевременная {subject} - корень всех зол. ({aut})")

# модификаторы форматирования
num = 8
print(f"Binary: {num:#b}")

op = 2 / 3
print(op)
print(f"{op:.5f}")

# встроенная функция "input()"
name = input("Введите свое имя: ")
print(f"Привет, {name}!")

# байтовые строки (bytes). b - литерал для объявления байтовой строки
ex_bytes = b"hello"
print(type(ex_bytes))

for element in ex_bytes:
    print(element)

# для преобразования в байты юникодной строки используется кодировка UTF 8
uniq_str = "привет"
enc_str = uniq_str.encode(encoding="utf-8")
print(enc_str)
print(type(enc_str))

# декодируем байты обратно в строку
dec_str = enc_str.decode()
print(dec_str)
