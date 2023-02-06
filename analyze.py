import numpy
import matplotlib.pyplot as mat

backLegSensorValues = numpy.load("data/BackLegData.npy")
mat.plot(backLegSensorValues)

mat.show()


