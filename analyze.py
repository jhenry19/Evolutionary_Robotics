import numpy
import matplotlib.pyplot as mat


def plotLegData():
    backLegSensorValues = numpy.load("data/backTA.npy")
    frontLegSensorValues = numpy.load("data/frontTA.npy")

    mat.plot(backLegSensorValues, label='Back Leg', linewidth=3)
    mat.plot(frontLegSensorValues, label='Front Leg')

    mat.legend()
    mat.show()


def plotSin():
    sin = numpy.load("data/SinGraph.npy")

    mat.plot(sin)

    mat.show()


plotLegData()
