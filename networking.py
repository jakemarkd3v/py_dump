def accept_connections (host,port,s)

conn,address = s.accept()
print(f "Connection succesful on" p: {address[0]})

send.command()

conn.close()


def send_command(conn):
    while true:
        cmd =input()