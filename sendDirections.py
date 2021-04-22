#!/bin/python3

import sys
import base64
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect('192.168.1.14', username='pi', password='raspberry')

direction = sys.argv[1]
if(direction=="left"):
    client.exec_command('sudo turnLeft.py')
elif(direction=="center"):
    client.exec_command('sudo turnCenter.py')
elif(direction=="right"):
    client.exec_command('sudo turnRight.py')

client.close()
    
