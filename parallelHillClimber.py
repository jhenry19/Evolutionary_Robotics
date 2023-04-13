import solution
import constants as c
import copy
import os


class PARALLEL_HILL_ClIMBER:

    def __init__(self):
        # Removes all temporary files at startup
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.POPULATION_SIZE):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.children = None

        # For analysis
        self.firstGeneration = True
        self.initialParentFitness = {}
        self.finalParentFitness = {}

    def Evolve(self):
        self.Evaluate(self.parents)

        for i in range(c.NUMBER_OF_GENERATIONS):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Print(self):
        for i in range(c.POPULATION_SIZE):
            print("parent:", self.parents[i].fitness, "--- child:", self.children[i].fitness)
        print("\n")

    def Spawn(self):
        self.children = {}
        for i in range(c.POPULATION_SIZE):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(c.POPULATION_SIZE):
            self.children[i].Mutate()

    def Evaluate(self, solutions):
        for i in range(c.POPULATION_SIZE):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.POPULATION_SIZE):
            solutions[i].Wait_For_Simulation_To_End()

        # Records the fitness of the first generation of parents for analysis
        if self.firstGeneration:
            for i in range(c.POPULATION_SIZE):
                self.initialParentFitness[i] = self.parents[i].fitness
            self.firstGeneration = False



    def Select(self):
        for i in range(c.POPULATION_SIZE):
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Show_Best(self):
        lowestScore = 99999.9
        lowestIndex = -1
        for i in range(c.POPULATION_SIZE):
            if self.parents[i].fitness < lowestScore:
                lowestScore = self.parents[i].fitness
                lowestIndex = i

        self.parents[lowestIndex].Start_Simulation("GUI")

    def analysis(self):
        averageImprovement = {}
        averageImprovementPerGeneration = {}
        sumOfImprovement = 0
        for i in range(c.POPULATION_SIZE):
            self.finalParentFitness[i] = self.parents[i].fitness

            averageImprovement[i] = abs(self.initialParentFitness[i] - self.finalParentFitness[i])
            sumOfImprovement += averageImprovement[i]
            averageImprovementPerGeneration[i] = averageImprovement[i] / c.NUMBER_OF_GENERATIONS






        averageImprovementForSimulation = sumOfImprovement / c.POPULATION_SIZE



        print(self.initialParentFitness)
        print(self.finalParentFitness)
        print(averageImprovement)
        print(averageImprovementPerGeneration)
        print(averageImprovementForSimulation)





