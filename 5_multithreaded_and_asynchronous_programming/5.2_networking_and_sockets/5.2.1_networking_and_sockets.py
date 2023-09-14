# сокеты - это кроссплатформенный механизм для обмена данными между процессами

import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем объект типа сокет
socket.bind(("localhost", 10001))   # регистрируем пару в ОС (Max port 65535)
socket.listen(socket.SOMAXCONN)     # начинаем принимать соединение

conn, addr = socket.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

conn.close()
socket.close()

# создание сокета, клиент
sock = socket.socket()
sock.connect((("localhost", 10001)))
sock.sendall("ping".encode("utf-8"))
sock.close()

# более короткая запись
sock = socket.create_connection(("localhost", 10001))
sock.sendall("ping".encode("utf-8"))
sock.close()

# создание сокета, контекстный менеджер
# сервер
with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            with True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf-8"))

# клиент
with socket.create_connection(("localhost", 10001)) as sock:
    sock.sendall("ping".encode("utf-8"))
