import math

import numpy as np
import matplotlib.pyplot as mat
import constants as c


class PLOT_FITNESS:
    def showGraph(self):
        ZeroHiddenFitnessValues = np.load("savedFiles/0HN_FitnessResults.npy")
        # OneHiddenFitnessValues = np.load("1HN_FitnessResults.npy")
        TwoHiddenFitnessValues = np.load("savedFiles/2HN_FitnessResults.npy")
        # ThreeHiddenFitnessValues = np.load("3HN_FitnessResults.npy")
        FourHiddenFitnessValues = np.load("savedFiles/4HN_FitnessResults.npy")

        # Set tick marks
        for i in range(self.numGenerations):
            self.xValues.append(i)
        mat.xticks(self.xValues[0::100])

        # for i in range(len(ZeroHiddenFitnessValues[0])):
        #     if i > 200:
        #         if ZeroHiddenFitnessValues[0][i] == 0:
        #             print(i)
        #             exit()
        self.zeros = self.getMeanOfEvolution(ZeroHiddenFitnessValues)
        self.twos = self.getMeanOfEvolution(TwoHiddenFitnessValues)
        self.fours = self.getMeanOfEvolution(FourHiddenFitnessValues)

        ###
        #  Show average lines
        ###
        # mat.plot(self.zeros, linewidth=1, label="0", color="blue")
        # # mat.plot(self.getMeanOfEvolution(OneHiddenFitnessValues), linewidth=2, label="1")
        # mat.plot(self.twos, linewidth=1, label="2", color="red")
        # # mat.plot(self.getMeanOfEvolution(ThreeHiddenFitnessValues), linewidth=4, label="3")
        # mat.plot(self.fours, linewidth=1, label="4", color="green")

        # Zeros
        model = np.polyfit(self.xValues, self.zeros, 4)
        predict = np.poly1d(model)
        mat.plot(self.xValues, predict(self.xValues), linewidth=3, color="blue", label="1")

        # Twos
        model = np.polyfit(self.xValues, self.twos, 4)
        predict = np.poly1d(model)
        mat.plot(self.xValues, predict(self.xValues), linewidth=3, color="red", label="2")

        # Fours
        model = np.polyfit(self.xValues, self.fours, 4)
        predict = np.poly1d(model)
        mat.plot(self.xValues, predict(self.xValues), linewidth=3, color="green", label="4")


        mat.ylim(-2, 0)
        mat.xlim(0, 1300)
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
                fitness = array[value][x]
                toMean.append(fitness)

            # toMean.sort()
            # toMean.remove(toMean[0])
            # toMean.remove(toMean[-1])
            means.append(np.mean(toMean))
            toMean.clear()

        return means

    def lineOfBestFit(self):
        # Preparing X and y from the given data

        array = []
        for i in range(len(self.zeros)):
            array.append([i, self.zeros[i]])
        # X = array[:, 0]
        # y = array[:, 1]


        # Calculating parameters (theta0, theta1 and theta2)
        # of the 2nd degree curve using the numpy.polyfit() function
        theta = np.polyfit(X, y, 2)

        print(f'The parameters of the curve: {theta}')

        # Now, calculating the y-axis values against x-values according to
        # the parameters theta0, theta1 and theta2
        self.y_line = theta[1] + theta[0] * X
        mat.plot(X, self.y_line, 'r')


    def __init__(self, numGenerations):
        self.y_line = None
        self.zeros = None
        self.twos = None
        self.fours = None
        self.xValues = []
        self.numGenerations = numGenerations
        self.showGraph()


PLOT_FITNESS(1300)
