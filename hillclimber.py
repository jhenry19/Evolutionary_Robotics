import solution
import constants as c


class HILL_ClIMBER:
    def Evolve(self):
        self.parent.Evaluate()
        for i in range(c.NUMBER_OF_GENERATIONS):
            self.Spawn()
            self.Mutate()
            self.child.Evaluate()
            self.Select()

    def __init__(self):
        self.child = None
        self.parent = solution.SOLUTION()

    def Spawn(self):
        pass

    def Mutate(self):
        pass

    def Select(self):
        pass


