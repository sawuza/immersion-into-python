import socket
import time


class ClientError(BaseException):
    pass


class Client:
    _instance = None

    def __new__(cls, host, port, timeout=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host, port, timeout=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        if timeout is not None:
            self.sock.settimeout(timeout)

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        self.sock.sendall("put {} {} {}\n".format(key, value, timestamp).encode("utf-8"))
        data = self.sock.recv(1024).decode("utf-8")
        data_split = data.split("\n")
        if data_split[0] != "ok":
            raise ClientError

    def get(self, key):
        self.sock.sendall("get {}\n".format(key).encode("utf-8"))
        data = self.sock.recv(1024).decode("utf-8")
        data_split = data.split("\n")
        data_dict = {}
        if data_split[0] != "ok":
            raise ClientError
        data_split = data_split[1:len(data_split) - 2]
        for i in data_split:
            elements = i.split(" ")
            if len(elements) < 3:
                raise ClientError
            if elements[0] not in data_dict:
                data_dict[elements[0]] = []
            try:
                data_dict[elements[0]].append((int(elements[2]), float(elements[1])))
                data_dict[elements[0]] = sorted(data_dict[elements[0]], key=lambda element: element[0])
            except Exception:
                raise ClientError
        if key == "*":
            return data_dict
        elif key in data_dict:
            return {key: data_dict[key]}
        else:
            return {}
