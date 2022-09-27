
import socket

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

getURL = input('Enter URL: ')
getERL = getURL.split('/')
words = getERL[2]
sockt.connect((words, 80))
sockt.send('GET ' + getURL + ' HTTP/1.0\n\n')
count = 0
while True:
    data = sockt.recv(512)
    if len(data) < 1:
        break
    count = count + len(data)
    print(data(3000))

print(count)
