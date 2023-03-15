import random

import solution
import constants as c
import copy


class HILL_ClIMBER:
    def Evolve(self):
        self.parent.Evaluate()
        for i in range(c.NUMBER_OF_GENERATIONS):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()
        self.Print()

    def Print(self):
        print("parent: ", self.parent.fitness, " --- child: ", self.child.fitness)

    def __init__(self):
        self.parent = solution.SOLUTION()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child


