import math

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random as rand

SIMULATION_STEPS = 100
amplitude = math.pi / 4.0
frequency = 1
phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

p.setGravity(0, 0, -9.8)  # set gravity

planeId = p.loadURDF("plane.urdf")  # loads floor
robotId = p.loadURDF("body.urdf")  # creates robot
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)  # sets up sensors
backLegSensorValues = numpy.zeros(SIMULATION_STEPS)
frontLegSensorValues = numpy.zeros(SIMULATION_STEPS)

# Create sin array
targetAngles = numpy.zeros(SIMULATION_STEPS)
x = numpy.linspace(0, 2 * numpy.pi, SIMULATION_STEPS)
for i in range(len(x)):
    targetAngles[i] = numpy.sin(x[i]) * math.pi / 4.0

# numpy.save("data/SinGraph", targetAngles)

for i in range(SIMULATION_STEPS):
    p.stepSimulation()

    # Store sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Motor
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAngles[i],
                                maxForce=20)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAngles[i],
                                maxForce=20)
    t.sleep(1 / 60)
p.disconnect()

numpy.save("data/BackLegData", backLegSensorValues)
numpy.save("data/FrontLegData", frontLegSensorValues)
