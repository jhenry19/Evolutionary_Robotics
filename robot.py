from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
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
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Values(self.robot, desiredAngle)

        self.t += 1  # increment the time step counter

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        # stateOfLinkZero = p.getLinkState(self.robot, 0)
        # positionOfLinkZero = stateOfLinkZero[0]
        # xCoordinateOfLinkZero = positionOfLinkZero[0]

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]


        # Due to threading, temp file is used for writing and then copied to a final fitness file
        f = open("tmp" + str(self.myID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()

        os.system("mv tmp" + str(self.myID) + ".txt fitness" + str(self.myID) + ".txt")

    def __init__(self, myID):
        # Initialize sensors and motors
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")  # creates robot

        pyrosim.Prepare_To_Simulate(self.robot)  # sets up sensors
        self.PrepareToSense()
        self.PrepareToAct()

        self.myID = myID

        self.nn = NEURAL_NETWORK("brain" + str(self.myID) + ".nndf")
        os.system("rm brain" + str(myID) + ".nndf")
