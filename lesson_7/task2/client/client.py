import socket
import rsa

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
data = "test_data".encode()

sock.send("key".encode())
public_key = sock.recv(1024)
public_key = rsa.PublicKey.load_pkcs1(public_key)

crypto = rsa.encrypt(data, public_key)
sock.send(crypto)
sock.close()