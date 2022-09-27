import socket
hostname = "www.google.com"

ip = socket.gethostbyhostname(hostname)
print(ip)
