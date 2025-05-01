import numpy as np
from fanucpy import Robot
import time

robot = Robot(
    robot_model="Fanuc",
    host="192.168.25.182",
    port=18735,
)

robot.__version__()

robot.connect()

print("Waiting 5 sek..")
time.sleep(5)
print("Start!")

for i in range(1,16):
    robot.set_do(i,True)
    time.sleep(1)

for i in range(1,16):
    robot.set_do(i,False)
    time.sleep(1)

robot.disconnect()
