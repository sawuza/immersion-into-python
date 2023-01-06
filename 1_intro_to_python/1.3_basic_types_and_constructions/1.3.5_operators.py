# оператор if используется для выполнения каких либо действий при выполнении условия
company = "my.com"

if "my" in company:
    print("Условие выполнено")

# оператор else выполняет какие либо действия, если условие if не выполняется
company = "google.com"

if "my" in company:
    print("Условие выполнено")
else:
    print("Условие не выполнено")

# оператор elif  используется когда нужно проверить несколько условий
if "my" in company:
    print("Условие выполнено")
elif "google" in company:
    print("Подстрока google найдена")
else:
    print("Условие не выполнено")

# аналог тернарного оператора
score_1 = 5
score_2 = 0

winner = "Argentina" if score_1 > score_2 else "Jamaica"
print(winner)

# оператор while выполняет блок когда пока выполняется условие
i = 1
while i < 10:
    i += 1

print(i)

# оператор for in позволяет проитерироваться по последовательности
name = "Alex"

for letter in name:
    print(letter)

# встроенный объект range(5) позволяет итерироваться по целым числам (начиная с 0 и до 5, не включая 5)
for num in range(5):
    print(num)

# задача Фридриха Гаусса. Получить сумму чисел от 0 до 100
result = 0

for i in range(0, 101):
    result += i

print(result)


# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# оператор pass, определяет пустой блок, который ничего не делает ( в основном используется в качестве заголуши)
for i in range(0, 100):
    pass

# оператор break, позволяет выйти из цикла досрочно
result = 0

while True:
    result += 1
    if result >= 100:
        break

print(result)


for i in range(10):
    if i == 5:
        break
    print(i)

# оператор continue позволяет перейти к следующей итерации в цикле без выполнения оставшихся инструкций
result = 0

for i in range(10):
    if i % 2 != 0:
        continue
    result += i

print(result)
