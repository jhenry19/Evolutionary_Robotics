# import constants as c
#
# import pybullet as p
# import time as t
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use
#
# p.setGravity(0, 0, c.GRAVITY)  # set gravity
#
# planeId = p.loadURDF("plane.urdf")  # loads floor
# robotId = p.loadURDF("body.urdf")  # creates robot
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate(robotId)  # sets up sensors
# backLegSensorValues = numpy.zeros(c.SIMULATION_STEPS)
# frontLegSensorValues = numpy.zeros(c.SIMULATION_STEPS)
#
# # Create sin array
# backTargetAngles = numpy.zeros(c.SIMULATION_STEPS)
# frontTargetAngles = numpy.zeros(c.SIMULATION_STEPS)
# for i in range(c.SIMULATION_STEPS):
#     backTargetAngles[i] = c.BACK_AMPLITUDE * numpy.sin(c.BACK_FREQUENCY / c.SIN_DIVISOR * i + c.BACK_PHASE_OFFSET)
#     frontTargetAngles[i] = c.FRONT_AMPLITUDE * numpy.sin(c.FRONT_FREQUENCY / c.SIN_DIVISOR * i + c.FRONT_PHASE_OFFSET)
#
# for i in range(c.SIMULATION_STEPS):
#     p.stepSimulation()
#
#     # Store sensor values
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
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
#     t.sleep(c.SLEEP_INCREMENT)
# p.disconnect()
#
# numpy.save("data/BackLegData", backLegSensorValues)
# numpy.save("data/FrontLegData", frontLegSensorValues)
pass
