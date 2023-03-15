import os
import hillclimber

# for i in range(1):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = hillclimber.HILL_ClIMBER()
hc.Evolve()
hc.Show_Best()

