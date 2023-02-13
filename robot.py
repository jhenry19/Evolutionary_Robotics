from sensor import SENSOR
from motor import MOTOR
class ROBOT:
    def __init__(self, s=2, m=2):
        # Initialize sensors and motors
        self.sensors = []
        self.motors = []
        for i in range(s):
            self.sensors[i] = SENSOR()
        for i in range(m):
            self.motors[i] = MOTOR()
