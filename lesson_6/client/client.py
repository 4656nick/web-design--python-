import socket


# Разработайте клиента и сервера, клиент будет запрашивать у пользователя название файла,
# а затем отправлять содержимое этого файла серверу.
# Сервер будет подсчитывать количество слов и возвращать ответ.

def open_txt_file_with_binary():
    filename = input("Введите имя файла: ")
    readByte = open(filename, "rb")
    data = readByte.read()
    readByte.close()
    return data


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))

sock.send(open_txt_file_with_binary())
response = sock.recv(1024).decode()
sock.close()

print(str(response))
