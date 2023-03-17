from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
myID = sys.argv[2]

simulation = SIMULATION(directOrGUI, myID)
simulation.Run()
simulation.Get_Fitness()
