import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 1 / 2


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[x - 5, y + 5, z], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[length, width, height])

    pyrosim.End()


# Create_World()
Create_Robot()