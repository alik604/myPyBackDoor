import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print("")
print("Server is currently running @", host)
print(" waiting for incoming connections")
s.listen(1)

conn, addr = s.accept()
print("")
print(addr, " Has connected")

# command handling

while 1:
    command = input(str("command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("waitng for execution")
        print("command executed")
        files = conn.recv(5000)
        files = files.decode()
        print("command output:",files)
    else:
        print("Command not recongnised")