#!/bin/python

import sys

actuator = __import__("actuator-drv8835")
actuator.init(55)

direction = sys.argv[1]
if(direction=="left"):
    actuator.left()
elif(direction=="center"):
    actuator.center()
elif(direction=="right"):
    actuator.right()
elif(direction=="forward"):
    actuator.ffw()
elif(direction=="backward"):
    actuator.rew()
elif(direction=="stop"):
    actuator.stop()

