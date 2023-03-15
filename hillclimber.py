import random

import solution
import constants as c
import copy


class HILL_ClIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for i in range(c.NUMBER_OF_GENERATIONS):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()


    def Print(self):
        print("\n\nparent:", self.parent.fitness, "--- child:", self.child.fitness, "\n\n")

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")



