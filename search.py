import os
import parallelHillClimber
import constants as c

phc = parallelHillClimber.PARALLEL_HILL_ClIMBER()
phc.Evolve()
# phc.analysis()
phc.Show_Best()


for i in range(c.POPULATION_SIZE * (1 + c.NUMBER_OF_GENERATIONS)):
    os.system("rm fitness" + str(i) + ".txt")


