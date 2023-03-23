import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time


class SOLUTION:
    def __init__(self, id):
        randomList = []
        arrayOfNumpyArrays = []
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                randomList.append(np.random.rand())

            arrayOfNumpyArrays.append(np.array(randomList))
            randomList.clear()

        self.weights = np.array(arrayOfNumpyArrays)
        print(self.weights)

        # self.weights = np.array([np.array([np.random.rand(), np.random.rand()]), np.array([np.random.rand(), np.random.rand()]),
        #      np.array([np.random.rand(), np.random.rand()])])
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

        # Front Leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, .5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[.2, 1, .2])

        # Back Leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[.2, 1, .2])

        # Left leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-.5, 0, 1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1, .2, .2])

        # Right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[.5, 0, 1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5, 0, 0], size=[1, .2, .2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        sensors = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg"]
        for i in range(len(sensors)):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=sensors[i])

        # Motor Neurons
        motors = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg"]
        for i in range(len(motors)):
            pyrosim.Send_Motor_Neuron(name=(i + c.numSensorNeurons), jointName=motors[i])

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
