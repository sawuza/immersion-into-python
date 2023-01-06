from random import randint

# генерируем целое число
number = randint(1,101)

# просим игрока ввести свое имя
name = input("Введите свое имя: ")

# выводим правила игры в консоль
print(f"""
Приветствую тебя {name}, сейчас мы сыграем с тобой в игру "Угадай число"
Я загадал целое  число от 1 до 100, а тебе предстоит его угадать
""")

# создаем бесконечный цикл
while True:

    # команда ввода числа игрока
    player_num = input("Введите ваше число: ")

    # выход из цикла
    if not player_num or player_num == "exit":
        break

    # проверка что пользователь ввел целое число
    if not player_num.isdigit():
        print("Введите правильное число")
        continue

    result = int(player_num)

    # проверка числа и вывод подсказки
    if result == number:
        print(f"Поздравляю {name} ! Вы угадали загаданное число.")
        break

    elif result < number:
        print(f"Загаданное число больше {player_num} ")
        continue

    elif result > number:
        print(f"Загаданное число меньше {player_num}")
        continue
