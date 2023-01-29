import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1

x = 1 / 2
y = 1 / 2
z = 1 / 2
pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[1 + x, y, 1 + z], size=[length, width, height])
pyrosim.End()
