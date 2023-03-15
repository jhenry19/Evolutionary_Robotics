import numpy
import math

# Environment
SIMULATION_STEPS = 200
# GRAVITY = -15
GRAVITY = -9.8
SLEEP_INCREMENT = 1 / 60

# BODY
length = 1
width = 1
height = 1

# Joints
MAX_FORCE = 30

# Movements
BACK_AMPLITUDE = math.pi / 4.0
BACK_FREQUENCY = 10
BACK_PHASE_OFFSET = 0
FRONT_AMPLITUDE = math.pi / 4.0
FRONT_FREQUENCY = 20
FRONT_PHASE_OFFSET = numpy.pi
SIN_DIVISOR = (SIMULATION_STEPS / 20 * math.pi)
