# https://www.youtube.com/watch?v=-goH6bhyxmA&feature=youtube_video_deck
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
    print("1: View cwd\n "
          "2: View custom Dir\n"
          "3: Download File \n"
          "4:   \n")

    command = input(str("command >> "))
    if command == "1":
        conn.send(command.encode())
        print("waitng for execution")
        print("command executed")
        files = conn.recv(5000)
        files = files.decode()
        print("command output:", files)

    elif command == "2":
        conn.send(command.encode())
        print("")
        userInput = input(str("Custom Dir: "))
        conn.send(userInput.encode())
        print("sent*")
        files = conn.recv(5000)
        files = files.decode()
        print("")
        print("custom dir: ", files)

    elif command == "3":
        conn.send(command.encode())
        print("")



    else:
        print("Command not recongnised")
