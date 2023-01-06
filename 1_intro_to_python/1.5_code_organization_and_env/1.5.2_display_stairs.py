import sys

digit_string = int(sys.argv[1])
h = 0

while True:
    if digit_string == 0:
        break
    else:
        digit_string -= 1
        h += 1
        print((" " * digit_string) + ("#" * h))
