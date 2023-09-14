# создание сокета, таймауты и обработка ошибок
# сервер
import socket


with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        conn, add = sock.accept()
        conn.settimeout(5)
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print("close connection by timeout")
                    break

                if not data:
                    break
                print(data.decode("utf-8"))


# клиент
with socket.create_connection(("localhost", 10001), 5) as sock:
    sock.settimeout(2)
    try:
        sock.sendall("ping".encode("utf-8"))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error", ex)
