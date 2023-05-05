import os
import parallelHillClimber
import constants as c
import time
import numpy as np
import plotFitnessValues as plot

GENERATIONS_PER_RUN = 10
MINUTES_TO_RUN = 420

secondsToRun = MINUTES_TO_RUN * 60
iterationsCompleted = 0

zero = parallelHillClimber.PARALLEL_HILL_ClIMBER(0)
two = parallelHillClimber.PARALLEL_HILL_ClIMBER(2)
four = parallelHillClimber.PARALLEL_HILL_ClIMBER(4)
populations = [zero, two, four]

###
# Delete files in previous run folder
###
directoryNames = ["0HN", "2HN", "4HN"]
for directory in directoryNames:
    for file in os.listdir(directory):
        os.system("rm " + os.path.join(directory, file))

start = time.time()
now = time.time()
running = True

os.system("say starting run")
while now - start <= secondsToRun:
    for phc in populations:
        phc.Evolve(GENERATIONS_PER_RUN, False)
        phc.SaveFitness()

    iterationsCompleted += 1
    now = time.time()
    print("Completed", str(iterationsCompleted), "runs")

for phc in populations:
    phc.SaveRunInfo()
    phc.Determine_Best()

# # Fitnesses are too long. Cuts the arrays to only what is needed
# for phc in populations:
#     phc.TrimFitness(iterationsCompleted)

totalGenerations = iterationsCompleted * GENERATIONS_PER_RUN
plot.PLOT_FITNESS(totalGenerations)



# os.system("say done with run")
# phc.analysis()
# phc.Show_Best()
