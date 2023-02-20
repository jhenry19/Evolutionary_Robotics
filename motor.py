import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c


class MOTOR:
    def Set_Values(self):
        pass

    def Prepare_To_Act(self):
        pass
        for i in range(c.SIMULATION_STEPS):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency / c.SIN_DIVISOR * i + self.offset)

        # pyrosim.Set_Motor_For_Joint(bodyIndex=self.robotId,
        #                             jointName=self.jointName,
        #                             controlMode=p.POSITION_CONTROL,
        #                             targetPosition= backTargetAngles[i],
        #                             maxForce=c.MAX_FORCE)

    def __init__(self, jointName):
        self.jointName = jointName
        self.amplitude = c.FRONT_AMPLITUDE
        self.frequency = c.FRONT_FREQUENCY
        self.offset = c.FRONT_PHASE_OFFSET
        self.motorValues = numpy.zeros(c.SIMULATION_STEPS)
        self.Prepare_To_Act()

