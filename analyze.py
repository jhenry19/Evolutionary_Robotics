import numpy
import matplotlib.pyplot as mat

backLegSensorValues = numpy.load("data/BackLegData.npy")
frontLegSensorValues = numpy.load("data/FrontLegData.npy")

mat.plot(backLegSensorValues, label='Back Leg', linewidth=3)
mat.plot(frontLegSensorValues, label='Front Leg')

mat.legend()
mat.show()


