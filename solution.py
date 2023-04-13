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
        # Creates a matrix of height #sensors + #motors + #hidden and width #hidden. The last part of the matrix is
        # for the self connections of hidden neurons and only the first column is used
        for i in range(c.numSensorNeurons + c.numMotorNeurons + c.numHiddenNeurons):
            for j in range(c.numHiddenNeurons):
                randomList.append(np.random.rand())

            arrayOfNumpyArrays.append(np.array(randomList))
            randomList.clear()


        self.weights = np.array(arrayOfNumpyArrays)

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

        # Front Lower Leg
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[.2, .2, 1])

        # Back Lower Leg
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[.2, .2, 1])

        # Left Lower Leg
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[.2, .2, 1])

        # Right Lower Leg
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[.2, .2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Sensor Neurons
        sensors = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg",
                   "FrontLowerLeg", "BackLowerLeg", "LeftLowerLeg", "RightLowerLeg"]
        for i in range(len(sensors)):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=sensors[i])

        # Hidden Neurons
        for i in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=len(sensors) + i)

        # Motor Neurons
        motors = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg",
                  "FrontLeg_FrontLowerLeg", "BackLeg_BackLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg"]
        for i in range(len(motors)):
            pyrosim.Send_Motor_Neuron(name=(i + c.numSensorNeurons + c.numHiddenNeurons), jointName=motors[i])

        # Synapses
        hiddenNeuronOffset = c.numSensorNeurons
        motorNeuronOffset = c.numSensorNeurons + c.numHiddenNeurons
        for sensor in range(c.numSensorNeurons):
            for hidden in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=hidden + hiddenNeuronOffset,
                                     weight=self.weights[sensor][hidden])

        for hidden in range(c.numHiddenNeurons):
            for motor in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=hidden + hiddenNeuronOffset,
                                     targetNeuronName=motor + motorNeuronOffset,
                                     weight=self.weights[motor + c.numSensorNeurons][hidden])

        # Add self-connections to all hidden neurons
        for hidden in range(c.numHiddenNeurons):
            for otherHidden in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=hidden + hiddenNeuronOffset,
                                     targetNeuronName=otherHidden + hiddenNeuronOffset,
                                     weight=self.weights[otherHidden + c.numSensorNeurons][hidden])

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
        randomRow = random.randint(0, c.numSensorNeurons + c.numMotorNeurons + c.numHiddenNeurons - 1)

        randomColumn = random.randint(0, c.numHiddenNeurons - 1)

        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
