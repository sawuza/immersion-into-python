from random import randint

num_win = int(input())
last_ticket = input().upper()

split_last_ticket = last_ticket.split(" ")
ticket_num = int(split_last_ticket[0])
ticket_series = split_last_ticket[1]

winners_list = []
counter = 0

while counter < min(num_win, ticket_num):
    winner = randint(1, ticket_num)
    if winner not in winners_list:
        winners_list.append(winner)
        counter += 1

res = []
for winner in winners_list:
    res.append('0' * (6 - len(str(winner))) + str(winner) + " " + ticket_series)

for i in range(0, len(res)):
    print("Победитель номер {a} - \"{b}\"".format(a=i + 1, b=res[i]))
