import numpy as np
import matplotlib.pyplot as mat
import constants as c


def showGraph():

    ZeroHiddenFitnessValues = np.load("0FitnessResults.npy")
    OneHiddenFitnessValues = np.load("1FitnessResults.npy")
    TwoHiddenFitnessValues = np.load("2FitnessResults.npy")
    ThreeHiddenFitnessValues = np.load("3FitnessResults.npy")
    # FourHiddenFitnessValues = np.load("4FitnessResults.npy")

    mat.plot(getMeanOfEvolution(ZeroHiddenFitnessValues), linewidth=1)
    mat.plot(getMeanOfEvolution(OneHiddenFitnessValues), linewidth=2)
    mat.plot(getMeanOfEvolution(TwoHiddenFitnessValues), linewidth=3)
    mat.plot(getMeanOfEvolution(ThreeHiddenFitnessValues), linewidth=4)
    # mat.plot(getMeanOfEvolution(FourHiddenFitnessValues), linewidth=5)
    mat.show()


def getMeanOfEvolution(array):
    toMean = []
    means = []
    for i in range(c.NUMBER_OF_GENERATIONS):
        for value in range(len(array)):
            toMean.append(array[value][i])
        means.append(np.mean(toMean))
        toMean.clear()

    return means


showGraph()
