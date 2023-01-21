import random

number = []
number_size = random.randint(10, 15)

for _ in range(number_size):
    number.append(random.randint(10, 20))
number.sort()

half_size = len(number) // 2
median = None

if number_size % 2 == 1:
    median = number[half_size]
else:
    median = sum(number[half_size - 1:half_size + 1]) / 2
print(median)
