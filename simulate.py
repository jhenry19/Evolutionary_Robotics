import pybullet as p
import time as t
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

p.setGravity(0, 0, -9.8)  # set gravity

planeId = p.loadURDF("plane.urdf")  # loads floor
p.loadSDF("boxes.sdf")

for i in range(1000):
    p.stepSimulation()
    t.sleep(1 / 60)
    print(i)
p.disconnect()
