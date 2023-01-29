import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1

x = 1 / 2
y = 1 / 2
z = 1 / 2

for r in range(3):
    for c in range(3):
        for n in range(10): # Creates one tower
            pyrosim.Send_Cube(name="Box", pos=[x + r, y + c, z + n], size=[length * (.9 ** n), width * (.9 ** n), height * (.9 ** n)])

pyrosim.End()
