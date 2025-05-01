import numpy as np
from fanucpy import Robot
import time
from threading import Thread, Event

robot = Robot(
    robot_model="Fanuc",
    host="192.168.25.182",
    port=18735,
)

logger = Robot(
    robot_model="Fanuc",
    host="192.168.25.182",
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
        time.sleep(0.1)

logger_thread = Thread(target=stream_jpos)
logger_thread.start()


# Get current joint positions
q_home = np.array(robot.get_curjpos())
print("Home position:", q_home)

# Trajectory settings
n_points = 100
amplitude_deg = 10
amplitude_rad = np.deg2rad(amplitude_deg)  # if needed for radians
frequencies = np.array([0.5, 0.8, 1.1, 1.4, 1.7, 2.0]) 

# Time vector
t_max = 5  # seconds
t = np.linspace(0, t_max, n_points)

# Sinusoidal joint trajectories
trajectory = []
for i in range(n_points):
    q = q_home.copy()
    for j in range(len(q)):
        q[j] += amplitude_deg * np.sin(2 * np.pi * frequencies[j] * t[i])
    trajectory.append(q.tolist())


# Execute trajectory from PR[1] to PR[n]
robot.joint_trajectory(trajectory)

logger_stop_event.set()
logger_thread.join()


