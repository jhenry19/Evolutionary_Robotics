import os
import hillclimber
import parallelHillClimber
import constants as c

# for i in range(1):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = parallelHillClimber.PARALLEL_HILL_ClIMBER()
phc.Evolve()
phc.Show_Best()

for i in range(c.POPULATION_SIZE * (1 + c.NUMBER_OF_GENERATIONS)):
    os.system("rm fitness" + str(i) + ".txt")


