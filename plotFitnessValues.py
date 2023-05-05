import numpy as np
import matplotlib.pyplot as mat
import constants as c


class PLOT_FITNESS:
    def showGraph(self):
        ZeroHiddenFitnessValues = np.load("0HN_FitnessResults.npy")
        # OneHiddenFitnessValues = np.load("1HN_FitnessResults.npy")
        TwoHiddenFitnessValues = np.load("2HN_FitnessResults.npy")
        # ThreeHiddenFitnessValues = np.load("3HN_FitnessResults.npy")
        FourHiddenFitnessValues = np.load("4HN_FitnessResults.npy")

        for i in range(len(ZeroHiddenFitnessValues)):
            print(ZeroHiddenFitnessValues[i][:self.numGenerations])
        # Set tick marks at each generation
        for i in range(self.numGenerations):
            self.xValues.append(i)
        mat.xticks(self.xValues)

        mat.plot(self.getMeanOfEvolution(ZeroHiddenFitnessValues), linewidth=1, label="0")
        # mat.plot(self.getMeanOfEvolution(OneHiddenFitnessValues), linewidth=2, label="1")
        mat.plot(self.getMeanOfEvolution(TwoHiddenFitnessValues), linewidth=3, label="2")
        # mat.plot(self.getMeanOfEvolution(ThreeHiddenFitnessValues), linewidth=4, label="3")
        mat.plot(self.getMeanOfEvolution(FourHiddenFitnessValues), linewidth=5, label="4")

        mat.xlabel("Generations")
        mat.ylabel("Fitness")
        mat.grid(axis='x', color='0.95')
        mat.legend()
        mat.title("Average Fitness with Changing Number of Hidden Neuron")
        mat.show()
        mat.savefig("fitness_graph.png")

    def getMeanOfEvolution(self, array):
        toMean = []
        means = []
        for x in self.xValues:
            for value in range(len(array)):
                toMean.append(array[value][x])
            means.append(np.mean(toMean))
            toMean.clear()

        return means

    def __init__(self, numGenerations):
        self.xValues = []
        self.numGenerations = numGenerations
        self.showGraph()
