import numpy as np
from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="192.168.234.2",
    port=18735,
)

robot.__version__()

robot.connect()

orientation = [0,0,0]

v_max = 500
cnt = 0

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
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
    linear=True,
)

robot.move(
    "pose",
    vals= [200,200,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
    linear=True,
)

robot.move(
    "pose",
    vals= [0,200,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
    linear=True,
)

robot.move(
    "pose",
    vals=[0,0,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
    linear=True,
)

robot.move(
    "pose",
    vals=[-100,0,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
    linear=True,
)

robot.circ(
    mid=[-71,71,0] + orientation,
    end=[0,100,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
)

robot.circ(
    mid=[71,71,0] + orientation,
    end=[100,0,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
)

robot.circ(
    mid=[71,-71,0] + orientation,
    end=[0,-100,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
)



robot.circ(
    mid=[-71,-71,0] + orientation,
    end=[-100,0,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
)

robot.move(
    "pose",
    vals=[0,0,0] + orientation,
    velocity=v_max,
    acceleration=100,
    cnt_val=cnt,
    linear=True,
)

robot.disconnect()