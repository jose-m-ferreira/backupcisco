import getpass
import telnetlib
import tftpy

import os
import threading
import sys
from threading import Thread


ciscoswitches = []

f = open('cisco_switches.list', 'r')
ciscoswitches3 = f.readlines()

for i in range(len(ciscoswitches3)):
    ciscoswitches.append(ciscoswitches3[i].strip('\n'))

f.close()
#print(ciscoswitches)

def starttftp():
    if not os.path.exists('configs'):
        os.makedirs('configs')
    while True:
        tftpserver = tftpy.TftpServer('configs')
        tftpserver.listen('0.0.0.0', 69)

        global stop_threads

        if stop_threads:
            tftpserver.shutdown_gracefully()
            break


def backup(host, user, password, localip):
    host = host
    user = user
    password = password
    localip = localip
    copystring = "copy run tftp://" + localip + "/" + host + ".cfg"
    print(copystring)

    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")

    tn.write(user.encode('ascii') + b"\n")

    tn.read_until(b"Password: ")

    tn.write(password.encode('ascii') + b"\n")
    #tn.read_until(b">")

    tn.write(b"enable\n")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(copystring.encode('ascii') + b"\n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
    tn.close()


def backupswitches():
    user = input("Enter User Name: ")
    password = getpass.getpass()
    localip = input("Enter TFTP server ip: ")

    for switch in ciscoswitches:
        backup(switch, user, password, localip)

stop_threads = False
tftp = threading.Thread(target=starttftp).start()
backupswitches()
stop_threads = True
sys.exit()


