import numpy as np
from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="127.0.0.1",
    port=18735,
)

robot.__version__()

robot.connect()

# get robot state
print("Current poses: ")
cur_jpos = robot.get_curjpos()
print(f"Current joints: {cur_jpos}")

# move in joint space
robot.move(
    "joint",
    vals=np.array(cur_jpos) + 0.5,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=False,
)

print("After: ")
cur_jpos = robot.get_curjpos()
print(f"Current joints: {cur_jpos}")
