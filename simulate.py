import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

p.setGravity(0, 0, -9.8)  # set gravity

planeId = p.loadURDF("plane.urdf")  # loads floor
torsoId = p.loadURDF("body.urdf") # creates robot
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(torsoId) # sets up sensors
for i in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    t.sleep(1 / 60)
    print(i)
p.disconnect()
