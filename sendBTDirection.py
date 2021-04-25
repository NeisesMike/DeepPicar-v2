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

# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = bluetooth.find_service(uuid=uuid, address=addr)

stamp1 = time.time()

if len(service_matches) == 0:
    print("Couldn't find the SampleServer service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))
stamp2 = time.time()

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

stamp3 = time.time()
sock.send("left")

stamp4 = time.time()

sock.close()


print("timing results:")
print(stamp1 - start)
print(stamp2 - stamp1)
print(stamp3 - stamp2)
print(stamp4 - stamp3)
