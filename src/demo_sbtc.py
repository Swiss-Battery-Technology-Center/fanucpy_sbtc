import numpy as np
from fanucpy import Robot
import time

from threading import Thread, Event

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


lpos = robot.get_lpos()

for i in range(2):
    lpos = robot.get_lpos()
    print(lpos)
    time.sleep(1)

position = lpos[:3]
orientation = lpos[3:]


# Digital outpus
for i in range(1, 5):
    robot.set_do(i, False)
    print(f"DO {i} set to False")
    time.sleep(0.5) 
    robot.set_do(i, True)
    print(f"DO {i} set to True")
    time.sleep(0.5)


# move in joint space
print("Move 1")
new_pos = (np.array(position) + np.array([200, 200, 200])).tolist()
robot.move(
    "pose",
    vals= new_pos + orientation,
    velocity=200,
    linear=False,
    cnt_val=100,
)

print("Move 3")
new_pos = (np.array(position) + np.array([0, -300, 200])).tolist()
robot.move(
    "pose",
    vals= new_pos + orientation,
    velocity=200,
    linear=True,
    cnt_val=100,
)

print("Move 4")
new_pos = (np.array(position) + np.array([0, -150, 200])).tolist()
robot.move(
    "pose",
    vals= new_pos + orientation,
    linear=True,
)

new_pos = (np.array(position)).tolist()
robot.move(
    "pose",
    vals= new_pos + orientation,
    velocity=200,
    linear=False,
)


logger_stop_event.set()
logger_thread.join()





# robot.move(
#     "pose",
#     vals= [200,0,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
#     linear=True,
# )

# robot.move(
#     "pose",
#     vals= [200,200,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
#     linear=True,
# )

# robot.move(
#     "pose",
#     vals= [0,200,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
#     linear=True,
# )

# robot.move(
#     "pose",
#     vals=[0,0,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
#     linear=True,
# )

# robot.move(
#     "pose",
#     vals=[-100,0,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
#     linear=True,
# )

# robot.circ(
#     mid=[-71,71,0] + orientation,
#     end=[0,100,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
# )

# robot.circ(
#     mid=[71,71,0] + orientation,
#     end=[100,0,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
# )

# robot.circ(
#     mid=[71,-71,0] + orientation,
#     end=[0,-100,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
# )



# robot.circ(
#     mid=[-71,-71,0] + orientation,
#     end=[-100,0,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
# )

# robot.move(
#     "pose",
#     vals=[0,0,0] + orientation,
#     velocity=v_max,
#     acceleration=100,
#     cnt_val=cnt,
#     linear=True,
# )

# robot.disconnect()