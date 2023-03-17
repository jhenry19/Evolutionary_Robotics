import random

import solution
import constants as c
import copy


class PARALLEL_HILL_ClIMBER:

    def __init__(self):
        self.parents = {}
        for i in range(c.POPULATION_SIZE):
            self.parents[i] = solution.SOLUTION()

    def Evolve(self):
        for i in range(c.POPULATION_SIZE):
            self.parents[i].Evaluate("GUI")
        # self.parent.Evaluate("GUI")
        # for i in range(c.NUMBER_OF_GENERATIONS):
        #     self.Evolve_For_One_Generation()

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
        pass
        # self.parent.Evaluate("GUI")



