#!/usr/bin/env python3

"""PyBluez simple example rfcomm-client.py
Simple demonstration of a client application that uses RFCOMM sockets intended
for use with rfcomm-server.
Author: Albert Huang <albert@csail.mit.edu>
$Id: rfcomm-client.py 424 2006-08-24 03:35:54Z albert $
"""

import sys

import bluetooth
import time


direction = sys.argv[1]

addr = None

#if len(sys.argv) < 2:
#    print("No device specified. Searching all nearby bluetooth devices for "
#          "the SampleServer service...")
#else:
#    addr = sys.argv[1]
#    print("Searching for SampleServer on {}...".format(addr))

start = time.time()


stamp1 = time.time()

stamp2 = time.time()

print(host)
print(port)

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("B8:27:EB:EC:85:F0", "1"))

stamp3 = time.time()
sock.send(direction)

stamp4 = time.time()

sock.close()


print("timing results:")
print(stamp1 - start)
print(stamp2 - stamp1)
print(stamp3 - stamp2)
print(stamp4 - stamp3)
