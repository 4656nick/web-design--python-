import socket


def count_words(data):
    return len(data.split())


server = socket.socket()
server.bind(('', 9090))
server.listen(1)
print("Сервер запущен...")

while True:
    conn, addr = server.accept()
    print('connected:', addr)
    data = conn.recv(1024).decode()
    if not data:
        break
    conn.send(str(count_words(data)).encode())