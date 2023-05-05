from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
myID = sys.argv[2]
numHiddenNeurons = sys.argv[3]

simulation = SIMULATION(directOrGUI, myID, numHiddenNeurons)
simulation.Run()
simulation.Get_Fitness()
