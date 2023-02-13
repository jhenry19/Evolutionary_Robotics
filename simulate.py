from simulation import SIMULATION


simulation = SIMULATION()
simulation.Run()


#
# # Create sin array
# backTargetAngles = numpy.zeros(c.SIMULATION_STEPS)
# frontTargetAngles = numpy.zeros(c.SIMULATION_STEPS)
# for i in range(c.SIMULATION_STEPS):
#     backTargetAngles[i] = c.BACK_AMPLITUDE * numpy.sin(c.BACK_FREQUENCY / c.SIN_DIVISOR * i + c.BACK_PHASE_OFFSET)
#     frontTargetAngles[i] = c.FRONT_AMPLITUDE * numpy.sin(c.FRONT_FREQUENCY / c.SIN_DIVISOR * i + c.FRONT_PHASE_OFFSET)
#
#
# p.disconnect()
#
# numpy.save("data/BackLegData", backLegSensorValues)
# numpy.save("data/FrontLegData", frontLegSensorValues)
