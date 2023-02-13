from sensor import SENSOR
from motor import MOTOR
import pybullet as p


class ROBOT:
    robotId = 0

    def __init__(self, s=2, m=2):
        # Initialize sensors and motors
        self.sensors = []
        self.motors = []
        for i in range(s):
            self.sensors.append(SENSOR())
        for i in range(m):
            self.motors.append(MOTOR())

        self.robotId = p.loadURDF("body.urdf")  # creates robot

