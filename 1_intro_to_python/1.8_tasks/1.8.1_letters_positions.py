a = input()
b = input()

lower_a = a.lower()
lower_b = b.lower()

uniq_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for item in lower_b:
    if item not in uniq_list and item in alphabet:
        uniq_list.append(item)


for letter_b in uniq_list:
    score = 1
    list_score = []

    for letter_a in lower_a:
        if letter_a == letter_b:
            list_score.append(score)
            score += 1
        else:
            score += 1

    if len(list_score) == 0:
        list_score.append(None)

    print(letter_b, " ".join(map(str, list_score)))
