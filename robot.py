from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c


class ROBOT:

    def PrepareToSense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

        self.t = 0  # time step counter

    def Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Values(self.t)

        self.t += 1  # increment the time step counter

    def PrepareToAct(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Values()





        # backTargetAngles = numpy.zeros(c.SIMULATION_STEPS)
        # frontTargetAngles = numpy.zeros(c.SIMULATION_STEPS)
        # for i in range(c.SIMULATION_STEPS):
        #     backTargetAngles[i] = c.BACK_AMPLITUDE * numpy.sin(
        #         c.BACK_FREQUENCY / c.SIN_DIVISOR * i + c.BACK_PHASE_OFFSET)
        #     frontTargetAngles[i] = c.FRONT_AMPLITUDE * numpy.sin(
        #         c.FRONT_FREQUENCY / c.SIN_DIVISOR * i + c.FRONT_PHASE_OFFSET)

    def __init__(self, s=2, m=2):
        # Initialize sensors and motors

        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")  # creates robot

        pyrosim.Prepare_To_Simulate(self.robotId)  # sets up sensors
        self.PrepareToSense()
        self.PrepareToAct()
