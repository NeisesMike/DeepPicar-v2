#!/usr/bin/env python3

import sys
import bluetooth
import time

direction = sys.argv[1]

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("B8:27:EB:EC:85:F0", 1))
sock.send(direction)
sock.close()

