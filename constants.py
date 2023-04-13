import numpy
import math

# Environment
SIMULATION_STEPS = 500
NUMBER_OF_GENERATIONS = 5
POPULATION_SIZE = 5
# GRAVITY = -15
GRAVITY = -9.8
SLEEP_INCREMENT = 1 / 200

# BODY
length = 1
width = 1
height = 1
numSensorNeurons = 9
numMotorNeurons = 8
motorJointRange = .5

# BRAIN
numHiddenNeurons = 5

# Joints
MAX_FORCE = 40

# Movements
BACK_AMPLITUDE = math.pi / 4.0
BACK_FREQUENCY = 10
BACK_PHASE_OFFSET = 0
FRONT_AMPLITUDE = math.pi / 4.0
FRONT_FREQUENCY = 20
FRONT_PHASE_OFFSET = numpy.pi
SIN_DIVISOR = (SIMULATION_STEPS / 20 * math.pi)
