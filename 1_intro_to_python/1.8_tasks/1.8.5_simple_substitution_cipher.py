input_str = input().lower()
input_cipher = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

dict_code = dict(zip(list(input_cipher), list(alphabet)))
res = ""

for i in input_str:
    if i in alphabet:
        res += dict_code[i]
    else:
        res += i

print(res)
