import numpy as np


class SOLUTION:
    def __init__(self):
        self.weights = np.array([np.array([np.random.rand(), np.random.rand()]), np.array([np.random.rand(), np.random.rand()]), np.array([np.random.rand(), np.random.rand()])])
        self.weights = self.weights * 2 - 1
