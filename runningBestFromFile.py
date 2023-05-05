import solution
import os
import numpy as np

###
# Populates a 2D array with all the final runs of a certain brain.
# todo: this is hella overcomplicated bc I we know the name of the file will be Best_Brain
###
directoryNames = ["0HN", "2HN", "4HN"]
brainFiles = []
for directoryIndex in range(len(directoryNames)):
    for file in os.listdir(directoryNames[directoryIndex]):
        if file == "Best_Brain.npy":
            brainFiles.append(os.path.join(directoryNames[directoryIndex], file))

###
# Run a solution from the brain in a text file
###
# Create 3 solutions
solutions = [solution.SOLUTION(0, 0), solution.SOLUTION(1, 2), solution.SOLUTION(2, 4)]

for solutionIndex in range(len(solutions)):
    solutions[solutionIndex].Simulation_With_Brain(np.load(brainFiles[solutionIndex]))
    print("\n\n" + str(solutions[solutionIndex].fitness))

