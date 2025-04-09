# fanucpy_sbtc: Python package for FANUC industrial robots with extra features

## Acknowledgements
This work is fork of [Xevi8X/fanucpy_extended](https://github.com/Xevi8X/fanucpy_extended) which is itself a fork of [torayeff/fanucpy](https://github.com/torayeff/fanucpy).

## Software contents
The package consists of two parts: 
1. Robot interface code written in Python programming language
2. FANUC robot controller driver (tested with R-30iA ver. 7.70) written in KAREL and FANUC teach pendant languages

## Usage
### Connect to a robot:
```python
from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="192.168.234.2",
    port=18735,
)

robot.connect()
```

### Moving
```python
# move in joint space
robot.move(
    "joint",
    vals=[19.0, 66.0, -33.0, 18.0, -30.0, -33.0],
    velocity=100,
    acceleration=100,
    cnt_val=0,
    linear=False
)

# move in cartesian space
robot.move(
    "pose",
    vals=[0.0, -28.0, -35.0, 0.0, -55.0, 0.0],
    velocity=50,
    acceleration=50,
    cnt_val=0,
    linear=False
)
```

### Querying robot state
```python
# get robot state
print(f"Current pose: {robot.get_curpos()}")
print(f"Current joints: {robot.get_curjpos()}")
print(f"Instantaneous power: {robot.get_ins_power()}")
print(f"Get gripper state: {robot.get_rdo(7)}")
```
