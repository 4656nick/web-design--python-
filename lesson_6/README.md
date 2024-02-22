***
Билд контейнера из папки ./server/:

**docker build . -t lesson6_web_design**

Запуск контейнера:

**docker run -d -p 9090:9090 lesson6_web_design:latest**

Запуск клиента:

**python3 ./client/client.py**
