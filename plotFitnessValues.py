import numpy as np
import matplotlib.pyplot as mat
import constants as c


def showGraph():
    ZeroHiddenFitnessValues = np.load("0FitnessResults.npy")
    OneHiddenFitnessValues = np.load("1FitnessResults.npy")
    TwoHiddenFitnessValues = np.load("2FitnessResults.npy")
    ThreeHiddenFitnessValues = np.load("3FitnessResults.npy")
    FourHiddenFitnessValues = np.load("4FitnessResults.npy")

    mat.plot(getMeanOfEvolution(ZeroHiddenFitnessValues), linewidth=1, label="0")
    mat.plot(getMeanOfEvolution(OneHiddenFitnessValues), linewidth=2, label="1")
    mat.plot(getMeanOfEvolution(TwoHiddenFitnessValues), linewidth=3, label="2")
    mat.plot(getMeanOfEvolution(ThreeHiddenFitnessValues), linewidth=4, label="3")
    mat.plot(getMeanOfEvolution(FourHiddenFitnessValues), linewidth=5, label="4")

    mat.xticks(xValues)

    mat.xlabel("Generations")
    mat.ylabel("Fitness")
    mat.grid(axis='x', color='0.95')
    mat.legend()
    mat.title("Average Fitness with Changing Number of Hidden Neuron")
    mat.show()


def getMeanOfEvolution(array):
    toMean = []
    means = []
    for x in xValues:
        for value in range(len(array)):
            toMean.append(array[value][x])
        means.append(np.mean(toMean))
        toMean.clear()

    return means

# Set tick marks at each generation
xValues = []
for i in range(c.NUMBER_OF_GENERATIONS):
    xValues.append(i)
showGraph()
