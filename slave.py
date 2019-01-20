import os
import socket

s = socket.socket()
port = 8080
host = input(str("enter server addr: "))

s.connect((host, port))

print("connected* ")

while 1:
    command = s.recv(1040)
    command = command.decode()
    print("command recived")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("command executed* ")
    else:
        print("Command not recongnised")
