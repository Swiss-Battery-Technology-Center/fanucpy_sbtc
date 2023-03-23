import numpy as np
from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="127.0.0.1",
    port=18735,
)

robot.__version__()

robot.connect()

orientation = [0,0,0]

# get robot state
print("Current poses: ")
cur_jpos = robot.get_curjpos()
print(f"Current joints: {cur_jpos}")

print("Setting PR[90] to 1,2,3,...")
robot.set_pr(90,[1,2,3,4,5,6])

print(f"Getting PR[91]: {robot.get_pr(91)}")

print(f"Getting R[91]: {robot.get_reg(90)}")


# move in joint space

robot.move(
    "pose",
    vals= [0,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=False,
)

robot.move(
    "pose",
    vals= [200,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=True,
)

robot.move(
    "pose",
    vals= [200,200,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=True,
)

robot.move(
    "pose",
    vals= [0,200,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=True,
)

robot.move(
    "pose",
    vals=[0,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=True,
)

robot.move(
    "pose",
    vals=[-100,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=True,
)

print("After: ")
cur_jpos = robot.get_curjpos()
print(f"Current joints: {cur_jpos}")
cur_pos = robot.get_curjpos()
print(f"Current cartesian: {cur_pos}")

robot.circ(
    mid=[-71,71,0] + orientation,
    end=[0,100,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
)

robot.circ(
    mid=[71,71,0] + orientation,
    end=[100,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
)

robot.circ(
    mid=[71,-71,0] + orientation,
    end=[0,-100,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
)


robot.circ(
    mid=[-71,-71,0] + orientation,
    end=[-100,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
)

robot.move(
    "pose",
    vals=[0,0,0] + orientation,
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=True,
)

robot.disconnect()