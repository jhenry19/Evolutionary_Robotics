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
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[c.length, c.width, c.height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Sensor Neurons
        # noinspection DuplicatedCode
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        sensors = ["Torso", "BackLeg", "FrontLeg"]

        # Motor Neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        motors = ["Torso_BackLeg", "Torso_FrontLeg"]

        # Synapses
        for currentRow in range(len(sensors)):
            for currentColumn in range(len(motors)):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=0.25)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=0.25)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-1.0)

        pyrosim.End()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        # Read in fitness value from txt only once simulation is done
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):  # waits for file to exist
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()

        os.system("rm " + fitnessFileName)

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1



