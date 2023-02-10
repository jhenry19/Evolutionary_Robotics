import math

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import matplotlib.pyplot as mat
import random as rand

SIMULATION_STEPS = 1000

###
# Moving robot with sin function
###
backAmplitude = math.pi / 4.0
backFrequency = 10
backPhaseOffset = 0
frontAmplitude = math.pi / 4.0
frontFrequency = 20
frontPhaseOffset = numpy.pi

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
backTargetAngles = numpy.zeros(SIMULATION_STEPS)
frontTargetAngles = numpy.zeros(SIMULATION_STEPS)
for i in range(SIMULATION_STEPS):
    backTargetAngles[i] = backAmplitude * numpy.sin(backFrequency / (SIMULATION_STEPS / 20 * math.pi) * i + backPhaseOffset)
    frontTargetAngles[i] = frontAmplitude * numpy.sin(frontFrequency / (SIMULATION_STEPS / 20 * math.pi) * i + frontPhaseOffset)

# numpy.save("data/backTA", backTargetAngles)
# numpy.save("data/frontTA", frontTargetAngles)

for i in range(SIMULATION_STEPS):
    p.stepSimulation()

    # Store sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Motor
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=backTargetAngles[i],
                                maxForce=15)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=frontTargetAngles[i],
                                maxForce=15)
    t.sleep(1 / 60)
p.disconnect()

numpy.save("data/BackLegData", backLegSensorValues)
numpy.save("data/FrontLegData", frontLegSensorValues)
