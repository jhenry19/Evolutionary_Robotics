import solution
import constants as c
import copy
import os
import numpy as np

MAX_GENERATIONS = 2000


class PARALLEL_HILL_ClIMBER:

    def __init__(self, numHiddenNeurons):
        # Removes all temporary files at startup
        os.system("rm brain*.nndf")
        os.system("rm " + str(numHiddenNeurons) + "HN_fitness*.txt")

        self.currentHiddenNeurons = numHiddenNeurons

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.POPULATION_SIZE):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID, self.currentHiddenNeurons)
            self.nextAvailableID += 1

        self.children = None

        # For AB Testing
        self.fitnessResults = np.zeros((c.POPULATION_SIZE, MAX_GENERATIONS))
        self.generationCount = 0
        self.print = False

    # Saves parents, next id, fitness results
    def SaveRunInfo(self):
        # Write next available id
        f = open(str(self.currentHiddenNeurons) + "HN/nextId.txt", "w")
        f.write(str(self.nextAvailableID))
        f.close()

        # save brains of each parents
        for i in range(c.POPULATION_SIZE):
            np.save(str(self.currentHiddenNeurons) + "HN/" + str(i) + "_Brain", np.array(self.parents[i].weights))

        filename = str(self.currentHiddenNeurons) + "FitnessResults"
        np.save(filename, self.fitnessResults)

    # Switch Context to run evolve another brain
    def PrepareForContextChange(self):
        # Saves current fitness values
        filename = str(self.currentHiddenNeurons) + "FitnessResults"
        np.save(filename, self.fitnessResults)

    def Evolve(self, numGenerations, shouldPrint):
        self.Evaluate(self.parents)
        self.print = shouldPrint
        for i in range(numGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        if self.print:
            self.Print()
        self.Select()
        self.generationCount += 1

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
            self.fitnessResults[i, self.generationCount] = solutions[i].fitness

        # # Records the fitness of the first generation of parents for analysis
        # if self.firstGeneration:
        #     for i in range(c.POPULATION_SIZE):
        #         self.initialParentFitness[i] = self.parents[i].fitness
        #     self.firstGeneration = False

    def Select(self):
        for i in range(c.POPULATION_SIZE):
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Determine_Best(self):
        lowestScore = 99999.9
        lowestIndex = -1
        for i in range(c.POPULATION_SIZE):
            if self.parents[i].fitness < lowestScore:
                lowestScore = self.parents[i].fitness
                lowestIndex = i

        np.save(str(self.currentHiddenNeurons) + "HN/" + "Best_Brain", np.array(self.parents[lowestIndex].weights))
        f = open(str(self.currentHiddenNeurons) + "HN/Best_Fitness.txt", "w")
        f.write(str(self.parents[lowestIndex].fitness))
        f.close()

        # self.parents[lowestIndex].Start_Simulation("GUI")

    def SaveFitness(self):
        filename = str(self.currentHiddenNeurons) + "HN_FitnessResults"

        # Save the fitness by converting it to a numpy array
        np.save(filename, np.array(self.fitnessResults))

    def TrimFitness(self, length):
        self.fitnessResults = self.fitnessResults[:length]
        self.SaveFitness()
