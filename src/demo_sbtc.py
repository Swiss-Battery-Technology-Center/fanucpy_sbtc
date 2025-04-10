import numpy as np
from fanucpy import Robot
import time

import spatialmath as sm
from threading import Thread, Event


def move_cartesian(robot: Robot, pose: sm.SE3, velocity: float = 200, linear: bool=False) -> None:
    position = list(pose.t * 1000) # Fanuc uses mm
    orientation = list(pose.rpy(unit="deg"))
    print(f"Moving to pose: \n{pose}")
    robot.move(
        "pose",
        vals=position + orientation,
        velocity=velocity,
        linear=linear,
    )

def get_pose(robot: Robot) -> sm.SE3:
    lpos = robot.get_lpos()
    position = np.array(lpos[:3]) / 1000 # Fanuc uses mm
    orientation = np.array(lpos[3:])
    return sm.SE3(position) * sm.SE3.RPY(orientation, unit="deg")


def set_vacuum(robot: Robot, enable: bool) -> None:
    do = 3
    if enable:
        robot.set_do(do, False)
    else:
        robot.set_do(do, True)

robot = Robot(
    robot_model="Fanuc",
    host="192.168.29.240",
    port=18735,
)

logger = Robot(
    robot_model="Fanuc",
    host="192.168.29.240",
    port=18736,
)

logger_stop_event = Event()

robot.__version__()

robot.connect()
logger.connect()

def stream_jpos():
    while not logger_stop_event.is_set():
        q = logger.get_curjpos()
        print(q)
        time.sleep(0.5)

logger_thread = Thread(target=stream_jpos)
logger_thread.start()




pose = get_pose(robot)
print(f"Current pose: {pose}")

set_vacuum(robot, False)

start_pose = sm.SE3(0.8, 0, 0.4) * sm.SE3.Rx(np.pi)
move_cartesian(robot, start_pose)

over_battery_pose = sm.SE3(-0.4, 1.0, 0.4) * sm.SE3.Rx(np.pi) * sm.SE3.Rz(-np.pi/2)
move_cartesian(robot, over_battery_pose)

pre_grasp_pose = sm.SE3(-0.4, 0.98, 0.05) * sm.SE3.Rx(np.pi) * sm.SE3.Rz(-np.pi/2)
move_cartesian(robot, pre_grasp_pose)

set_vacuum(robot, True)

grasp_pose = pre_grasp_pose * sm.SE3(0, 0, 0.08)
move_cartesian(robot, grasp_pose, velocity=20, linear=True)

# Move back
move_cartesian(robot, pre_grasp_pose, velocity=20, linear=True)
move_cartesian(robot, over_battery_pose, velocity=50)
move_cartesian(robot, start_pose)

set_vacuum(robot, False)




logger_stop_event.set()
logger_thread.join()



