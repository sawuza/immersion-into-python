import sys

digit_string = sys.argv[1]
num_list = []
for num in digit_string:
    num_list.append(int(num))

print(sum(num_list))
