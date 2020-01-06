import numpy as np
import sys
import random


numOfMachines = 4
tasks = []


class Task:
    def __init__(self, id, processingTime, readyTime, dueDate):
        self.id = id
        self.processingTime = processingTime
        self.readyTime = readyTime
        self.dueDate = dueDate

# populationMember represents a whole sequence
class populationMember:
    def __init__(self, sequenceOfTasksOnMachines):
        self.sequenceOfTasksOnMachines = sequenceOfTasksOnMachines

    def mutate(self):
        machineId = random.randint(0, numOfMachines)
        taskId = random.randint(0, len(self.sequenceOfTasksOnMachines[machineId]))
        
        # Task that we chose to move somewhere else
        taskChosen = self.sequenceOfTasksOnMachines[machineId][taskId]

        # remove the task from machine
        self.sequenceOfTasksOnMachines.remove(taskChosen)

        machineIdToPut = random.randint(0, numOfMachines)
        taskIdToPut = random.randint(0, len(self.sequenceOfTasksOnMachines[machineId]))

        # put the chosen task there
        #TODO: check if this actually works as insert was not in intellisense
        self.sequenceOfTasksOnMachines[machineIdToPut].insert(taskIdToPut, taskChosen)

        # I dont think there is need to fix those, nothing should be broken

def loadData(inputPath):
    array = []
    # dodac prawdziwe otwieranie pliku
    with open(inputPath, 'r') as file:
        N = int(file.readline())
        for i in range (0, N):
            one = file.readline().split()
            task = Task(i, one[0], one[1], one[2])
            array.append(task)

def fixSequence(sequenceOfTasksOnMachines):
    dupa = 0
    #TODO: iterate over the tasks in sequence and remove duplicates. Add all missing to the end on random machines

def crossover(firstPopulationMember, otherPopulationMember):
    firstSequence = firstPopulationMember.sequenceOfTasksOnMachines
    otherSequence = otherPopulationMember.sequenceOfTasksOnMachines

    #TODO: might not work as this returns array not tuple
    onMachine0first = np.split(firstSequence[0], len(firstSequence[1]) // 2 )
    onMachine1first = np.split(firstSequence[1], len(firstSequence[1]) // 2 )
    onMachine2first = np.split(firstSequence[2], len(firstSequence[2]) // 2 )
    onMachine3first = np.split(firstSequence[3], len(firstSequence[3]) // 2 )

    onMachine0other = np.split(otherSequence[0], len(otherSequence[1]) // 2 )
    onMachine1other = np.split(otherSequence[1], len(otherSequence[1]) // 2 )
    onMachine2other = np.split(otherSequence[2], len(otherSequence[2]) // 2 )
    onMachine3other = np.split(otherSequence[3], len(otherSequence[3]) // 2 )

    #stitch them together
    firstChildSequenceOnMachines = [onMachine0first[0] + onMachine0other[1],
                                    onMachine1first[0] + onMachine1other[1],
                                    onMachine2first[0] + onMachine2other[1],
                                    onMachine3first[0] + onMachine3other[1]]

    secondChildSequenceOnMachines = [onMachine0other[0] + onMachine0first[1],
                                     onMachine1other[0] + onMachine1first[1],
                                     onMachine2other[0] + onMachine2first[1],
                                     onMachine3other[0] + onMachine3first[1]]

    firstChildSequenceOnMachines = np.asarray(firstChildSequenceOnMachines)
    secondChildSequenceOnMachines = np.asarray(secondChildSequenceOnMachines)

    #TODO: pass those to fixSequence
    #TODO: create populationMembers from those



