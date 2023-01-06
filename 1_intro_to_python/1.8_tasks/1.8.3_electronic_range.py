shots = int(input())
total = 0

for d in range(0, shots):
    cords = input().split(" ")
    gep = (float(cords[0]) ** 2 + float(cords[1]) ** 2) ** 0.5
    if gep <= 10:
        total += 10 - int(gep)

print(total)
