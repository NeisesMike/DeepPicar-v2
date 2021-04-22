#!/bin/python3

import sys
import base64
import paramiko

direction = sys.argv[1]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('192.168.1.14', username='pi', password='raspberry')
stdin, stdout, stderr = client.exec_command('sudo takeDirection.py ' + direction)
for line in stderr:
    print('... ' + line.strip('\n'))
client.close()
    
