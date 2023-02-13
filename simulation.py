
import constants as c

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
from world import WORLD
from robot import ROBOT



class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

        p.setGravity(0, 0, c.GRAVITY)  # set gravity

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):

        for i in range(c.SIMULATION_STEPS):
            p.stepSimulation()
            ROBOT.Sense(self.robot)
            #
            #
            #     # Motor
            #     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
            #                                 jointName="Torso_BackLeg",
            #                                 controlMode=p.POSITION_CONTROL,
            #                                 targetPosition=backTargetAngles[i],
            #                                 maxForce=c.MAX_FORCE)
            #     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
            #                                 jointName="Torso_FrontLeg",
            #                                 controlMode=p.POSITION_CONTROL,
            #                                 targetPosition=frontTargetAngles[i],
            #                                 maxForce=c.MAX_FORCE)
            t.sleep(c.SLEEP_INCREMENT)

        # Destructor
        def __del__(self):
            p.disconnect()
