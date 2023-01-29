import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1

x = 1 / 2
y = 1 / 2
z = 1 / 2

for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x, y, z + i], size=[length * (.9 ** i), width * (.9 ** i), height * (.9 ** i)])

pyrosim.End()
