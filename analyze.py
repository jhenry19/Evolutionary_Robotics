import numpy
import matplotlib.pyplot as mat
import constants as c


def plotLegData():
    backLegSensorValues = numpy.load("data/backTA.npy")
    frontLegSensorValues = numpy.load("data/frontTA.npy")

    mat.plot(backLegSensorValues, label='Back Leg', linewidth=3)
    mat.plot(frontLegSensorValues, label='Front Leg')

    mat.legend()
    mat.show()


def plotSin():
    motorValues = numpy.empty(c.SIMULATION_STEPS)

    for i in range(c.SIMULATION_STEPS):
        motorValues[i] = c.FRONT_AMPLITUDE * numpy.sin(c.FRONT_FREQUENCY / c.SIN_DIVISOR * i + c.FRONT_PHASE_OFFSET)

    mat.plot(motorValues)

    mat.show()


plotSin()
