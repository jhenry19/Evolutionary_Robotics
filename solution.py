import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c


class SOLUTION:
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
        pyrosim.Start_NeuralNetwork("brain.nndf")
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
        for currentRow in range(len(sensors)):
            for currentColumn in range(len(motors)):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=0.25)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=0.25)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-1.0)

        pyrosim.End()

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def __init__(self):
        self.weights = np.array(
            [np.array([np.random.rand(), np.random.rand()]), np.array([np.random.rand(), np.random.rand()]),
             np.array([np.random.rand(), np.random.rand()])])
        self.weights = self.weights * 2 - 1

