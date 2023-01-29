import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 1/2

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[x - 5, y + 5, z], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position=[.5, 0, 1])
    pyrosim.Send_Cube(name="Leg", pos=[.5, y, z], size=[length, width, height])

    pyrosim.End()

Create_World()
Create_Robot()
