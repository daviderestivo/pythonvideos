#!/usr/bin/env python3

import telnetlib
import getpass

#  List of switches
hosts = ("192.168.0.1",)

def get_config(host, username, password):
        HOST = host.strip()
        try:
                tn = telnetlib.Telnet(HOST)
                print("Successfully connected to: " + host)
                print ("Getting current config of: " + host)
                tn.read_until(b"Username: ")
                tn.write(username.encode('ascii') + b"\n")
                if password:
                        tn.read_until(b"Password: ")
                        tn.write(password.encode('ascii') + b"\n")

                tn.write(b"terminal length 0\n")
                tn.write(b"show run\n")
                tn.write(b"exit\n")
                tn.close()

                readoutput = tn.read_all().decode('ascii')
                saveoutput = open("switch-" + HOST, "w+")
                saveoutput.write(readoutput)
                saveoutput.write("\n")
                saveoutput.close
        except OSError as err:
                print("OS error: {0}".format(err))

if __name__ == "__main__":
        # Get username and password
        username = input("Enter your username: ")
        password = getpass.getpass()
        #  Telnet to each switch and configure it
        for host in hosts:
                get_config(host, username, password)
