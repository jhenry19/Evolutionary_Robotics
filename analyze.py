import numpy as np
import matplotlib.pyplot as mat
import constants as c

fitnessValues = np.load("preliminaryResults/3FitnessResults.npy")
print(fitnessValues)

mat.plot(fitnessValues)
mat.show()


