import numpy
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def Get_Values(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if t == c.SIMULATION_STEPS - 1:
            print(self.values)

    def __init__(self, linkName):
        self.linkName = linkName

        self.values = numpy.zeros(c.SIMULATION_STEPS)

