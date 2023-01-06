my_input = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

uniq_list = []

for letter in my_input:
    if letter not in uniq_list and letter in alphabet:
        uniq_list.append(letter)

final_list = sorted(uniq_list)
print(''.join(final_list))
