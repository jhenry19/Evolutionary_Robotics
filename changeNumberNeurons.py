import os
import parallelHillClimber
import constants as c

numNeural = 5
for i in range(numNeural):
    print("RUNNING with", str(i), "hidden neurons")
    os.system("say running with " + str(i) + "hidden neurons")
    phc = parallelHillClimber.PARALLEL_HILL_ClIMBER(i)
    phc.Evolve()
    phc.SaveFitnesses()
    for j in range(c.POPULATION_SIZE * (1 + c.NUMBER_OF_GENERATIONS)):
        os.system("rm fitness" + str(j) + ".txt")
os.system("say done with run")
# phc.analysis()
# phc.Show_Best()
