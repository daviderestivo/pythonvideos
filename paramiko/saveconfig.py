#!/usr/bin/env python3

import paramiko
import getpass
import time

hosts = ("192.168.0.1",)

def get_config(host, username, password):
        HOST = host.strip()
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip_address,username=username,password=password)
            print("Successfully connected to: " + ip_address)
            print ("Getting current config of: " + host)
            remote_connection = ssh_client.invoke_shell()
            ("router ospf 1\n")
            remote_connection.send(b"terminal length 0\n")
            remote_connection.send(b"show run\n")
            remote_connection.send(b"exit\n")

            readoutput = remote_connection.recv(65535).decode('ascii')
            ssh_client.close()

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
