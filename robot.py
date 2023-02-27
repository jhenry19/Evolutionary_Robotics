from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
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

    def PrepareToAct(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                print(neuronName)

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Values(self.robotId, self.t)

        self.t += 1  # increment the time step counter

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def __init__(self, s=2, m=2):
        # Initialize sensors and motors
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")  # creates robot

        pyrosim.Prepare_To_Simulate(self.robotId)  # sets up sensors
        self.PrepareToSense()
        self.PrepareToAct()

        self.nn = NEURAL_NETWORK("brain.nndf")
