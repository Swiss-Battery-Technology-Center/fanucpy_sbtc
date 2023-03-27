import numpy as np
from fanucpy import Robot
import time

robot = Robot(
    robot_model="Fanuc",
    host="192.168.234.2",
    port=18736,
)

robot.__version__()

robot.connect()

while(True):
    print(f' Cur pos: {robot.get_curpos()}')
    print(f' Forces: {robot.get_forces()}')
    time.sleep(0.2)