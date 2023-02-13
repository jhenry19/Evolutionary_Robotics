from world import WORLD
from robot import ROBOT

import constants as c

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

        p.setGravity(0, 0, c.GRAVITY)  # set gravity

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(ROBOT.robotId)  # sets up sensors
