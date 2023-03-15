import solution


class HILL_ClIMBER:
    def Evolve(self):
        self.parent.Evaluate()

    def __init__(self):
        self.parent = solution.SOLUTION()


