# объект None  используется для того чтобы подчеркнуть отсутствие значения
answer = None
print(type(answer))

# bool(answer) = False ->
if not answer:
    # так как if not answer всегда будет True
    print("Ответ не получен")

income = None

if income is None:
    print("Еще не начали продавать")
elif not income:
    print("Ничего не заработали")
