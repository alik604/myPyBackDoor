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
    if command == "1":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("command executed* ")

    elif command == "2":
        userInput = s.recv(5000)
        userInput = userInput.decode()
        files = os.listdir(userInput)
        files = str(files)
        s.send(files.encode())
        print("cus dir sent done* ")

    elif command == "3":
        conn.send(command.encode())
        print("")

    else:
        print("Command not recongnised")
