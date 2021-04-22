#!/bin/python

import sys

actuator = __import__("actuator-drv8835")

direction = sys.argv[1]
if(direction=="left"):
    actuator.left()
elif(direction=="center"):
    actuator.center()
elif(direction=="right"):
    actuator.right()

