import rsa
import socket

db = [

]
server_port = 9090
server = socket.socket()
server.bind(('', server_port))
server.listen(1)
print(f"Сервер запущен на порту {server_port}...")
(public_key, private_key) = rsa.newkeys(1024)

while True:
    conn, addr = server.accept()
    print('connected:', addr)
    first_message = conn.recv(1024).decode()
    if first_message == 'key':
        conn.send(public_key.save_pkcs1().decode().encode())
        data = conn.recv(1024)
        data = rsa.decrypt(data, private_key)
        print(data.decode())
        conn.send(data)