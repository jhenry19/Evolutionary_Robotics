import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time


class SOLUTION:
    def __init__(self, id):
        self.weights = np.array(
            [np.array([np.random.rand(), np.random.rand()]), np.array([np.random.rand(), np.random.rand()]),
             np.array([np.random.rand(), np.random.rand()])])
        self.weights = self.weights * 2 - 1
        self.fitness = None

        self.myID = id

    def Set_ID(self, id):
        self.myID = id

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[c.length, c.width, c.height])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, .5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[.2, 1, .2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[.2, 1, .2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        sensors = ["Torso", "BackLeg", "FrontLeg"]

        # Motor Neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        motors = ["Torso_BackLeg", "Torso_FrontLeg"]

        # Synapses
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        # Read in fitness value from txt only once simulation is done
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):  # waits for file to exist
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
