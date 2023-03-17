import os
import hillclimber
import parallelHillClimber

# for i in range(1):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = parallelHillClimber.PARALLEL_HILL_ClIMBER()
phc.Evolve()
phc.Show_Best()

