from simulation import SIMULATION


simulation = SIMULATION()


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
