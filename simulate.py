import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

p.setGravity(0, 0, -9.8)  # set gravity

planeId = p.loadURDF("plane.urdf")  # loads floor
torsoId = p.loadURDF("body.urdf")  # creates robot
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(torsoId)  # sets up sensors
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    t.sleep(1 / 10)
p.disconnect()

numpy.save("data/BackLegData", backLegSensorValues)
numpy.save("data/FrontLegData", frontLegSensorValues)
