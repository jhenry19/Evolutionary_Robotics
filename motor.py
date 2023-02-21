import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c


class MOTOR:
    def Set_Values(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=self.motorValues[t],
                                    maxForce=c.MAX_FORCE)

    def Save_Values(self):
        numpy.save("data/" + self.jointName, self.motorValues)

    def Prepare_To_Act(self):
        self.amplitude = c.FRONT_AMPLITUDE
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.FRONT_FREQUENCY / 2.0
        else:
            self.frequency = c.FRONT_FREQUENCY
        self.offset = c.FRONT_PHASE_OFFSET
        for i in range(c.SIMULATION_STEPS):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency / c.SIN_DIVISOR * i + self.offset)

    def __init__(self, jointName):
        self.jointName = jointName

        # Initialize variables for sin curve of motor values
        self.offset = 0
        self.frequency = 0
        self.amplitude = 0
        self.motorValues = numpy.zeros(c.SIMULATION_STEPS)

        self.Prepare_To_Act()
