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
            ssh_client.connect(hostname=HOST,username=username,password=password)
            print("Successfully connected to: " + HOST)
            print ("Getting current config of: " + HOST)
            remote_connection = ssh_client.invoke_shell()
            remote_connection.send("terminal length 0\n")
            time.sleep(1)
            # Strip commands output
            remote_connection.recv(65535)
            # Get running-config
            remote_connection.send("show run\n")
            time.sleep(1)
            remote_connection.send("exit\n")

            readoutput = remote_connection.recv(65535).decode('ascii')
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
