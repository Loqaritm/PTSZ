import numpy as np
import sys
import random
from List_algorithm import ListAlgorithm


numOfMachines = 4
nonValue = 'emp'
tasks = []
globalShouldLog = True
# maxLen = 100

populationSize = 15
population = [0] * populationSize

def log(shouldLog, *arguments):
    if (shouldLog and globalShouldLog):
        print(arguments)

class Task:
    def __eq__(self, other):
        return self.id==other.id

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        return self.id
    
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "<Task id:%s>" % (self.id)

    def __init__(self, id, processingTime, readyTime, dueDate):
        self.id = id
        self.processingTime = processingTime
        self.readyTime = readyTime
        self.dueDate = dueDate

# populationMember represents a whole sequence
class PopulationMember:
    def __init__(self, sequenceOfTasksOnMachines):
        self.sequenceOfTasksOnMachines = sequenceOfTasksOnMachines

def mutate(populationMember):
    sequenceOfTasksOnMachines = populationMember.sequenceOfTasksOnMachines[:]

    machineId = random.randint(0, numOfMachines-1)
    taskId = random.randint(0, len(sequenceOfTasksOnMachines[machineId])-1)
    
    # Task that we chose to move somewhere else
    taskChosen = sequenceOfTasksOnMachines[machineId][taskId]

    # remove the task from machine
    sequenceOfTasksOnMachines[machineId].remove(taskChosen)

    machineIdToPut = random.randint(0, numOfMachines-1)
    taskIdToPut = random.randint(0, len(sequenceOfTasksOnMachines[machineId])-1)

    # put the chosen task there
    #TODO: check if this actually works as insert was not in intellisense
    sequenceOfTasksOnMachines[machineIdToPut].insert(taskIdToPut, taskChosen)
    return PopulationMember(sequenceOfTasksOnMachines)
    # I dont think there is need to fix those, nothing should be broken

def loadData(inputPath):
    array = []
    # dodac prawdziwe otwieranie pliku
    with open(inputPath, 'r') as file:
        N = int(file.readline())
        for i in range (0, N):
            one = file.readline().split()
            task = Task(i + 1, one[0], one[1], one[2])
            array.append(task)
    
    return array

def fixSequenceOfTasksOnMachines(sequenceOfTasksOnMachines, shouldLog = False):
    # create np array
    lens = [len(x) for x in sequenceOfTasksOnMachines]
    maxLen = max(lens)
    array = np.full((len(sequenceOfTasksOnMachines), maxLen), nonValue, Task)
    
    mask = np.arange(maxLen) < np.array(lens)[:,None] # key line
    array[mask] = np.concatenate(sequenceOfTasksOnMachines)
    # log(shouldLog, 'element 0:', array[0,0].id)

    # flatten and remove duplicates
    flattened = array.flatten()
    log(shouldLog, 'flattened:', flattened)
    flattened = [x for x in flattened if type(x) != type(nonValue)]
    log(shouldLog, 'flattened after removing non values:', flattened, len(flattened))
    withoutDuplicates = np.unique(flattened)
    log(shouldLog, 'without duplicates:', withoutDuplicates, len(withoutDuplicates))

    # fix missing ones
    missingValues = [x for x in tasks if x not in withoutDuplicates]
    log(shouldLog, [x.id for x in tasks if x not in withoutDuplicates])
    # log(shouldLog, 'Missing values found. At [0] is:', missingValues[0].id)

    np.random.shuffle(missingValues)
    log(shouldLog, [x.id for x in missingValues], len(missingValues))

    lenMissingValuesQuart = len(missingValues) // 4
    splitMissingTasks = np.split(missingValues, [lenMissingValuesQuart, 2* lenMissingValuesQuart, 3 * lenMissingValuesQuart])
    log(shouldLog, splitMissingTasks)

    # put the tasks on machines
    sequenceOfTasksOnMachines = [np.append(sequenceOfTasksOnMachines[i], splitMissingTasks[i]) for (i, line) in enumerate(sequenceOfTasksOnMachines)]
    return sequenceOfTasksOnMachines

def crossover(firstPopulationMember, otherPopulationMember):
    firstSequence = firstPopulationMember.sequenceOfTasksOnMachines
    otherSequence = otherPopulationMember.sequenceOfTasksOnMachines

    #TODO: might not work as this returns array not tuple

    parent1left = [[], [], [], []]
    parent1right = [[], [], [], []]
    parent2left = [[], [], [], []]
    parent2right = [[], [], [], []]

    child1 = [[], [], [], []]
    child2 = [[], [], [], []]

    for i in range(len(firstSequence)):
        child1[i] = firstSequence[i][0:len(firstSequence[i])//2] + otherSequence[i][len(otherSequence[i])//2:]
        child2[i] = otherSequence[i][0:len(otherSequence[i])//2] + firstSequence[i][len(firstSequence[i])//2:]

        # parent1left[i] = firstSequence[i][0:len(firstSequence[i])//2]
        # parent1right[i] = firstSequence[i][len(firstSequence[i])//2:]

        # parent2left[i] = otherSequence[i][0:len(otherSequence[i])//2]
        # parent2right[i] = otherSequence[i][len(otherSequence[i])//2:]



    # onMachine0first = np.split(firstSequence[0], len(firstSequence[1]) // 2 )
    # onMachine1first = np.split(firstSequence[1], len(firstSequence[1]) // 2 )
    # onMachine2first = np.split(firstSequence[2], len(firstSequence[2]) // 2 )
    # onMachine3first = np.split(firstSequence[3], len(firstSequence[3]) // 2 )

    # onMachine0other = np.split(otherSequence[0], len(otherSequence[1]) // 2 )
    # onMachine1other = np.split(otherSequence[1], len(otherSequence[1]) // 2 )
    # onMachine2other = np.split(otherSequence[2], len(otherSequence[2]) // 2 )
    # onMachine3other = np.split(otherSequence[3], len(otherSequence[3]) // 2 )

    # #stitch them together
    # firstChildSequenceOnMachines = [onMachine0first[0] + onMachine0other[1],
    #                                 onMachine1first[0] + onMachine1other[1],
    #                                 onMachine2first[0] + onMachine2other[1],
    #                                 onMachine3first[0] + onMachine3other[1]]

    # secondChildSequenceOnMachines = [onMachine0other[0] + onMachine0first[1],
    #                                  onMachine1other[0] + onMachine1first[1],
    #                                  onMachine2other[0] + onMachine2first[1],
    #                                  onMachine3other[0] + onMachine3first[1]]

    # firstChildSequenceOnMachines = np.asarray(firstChildSequenceOnMachines)
    # secondChildSequenceOnMachines = np.asarray(secondChildSequenceOnMachines)

    #TODO: create populationMembers from those

    firstChildSequenceOnMachines = fixSequenceOfTasksOnMachines(child1, False)
    secondChildSequenceOnMachines = fixSequenceOfTasksOnMachines(child2, False)

    return PopulationMember(firstChildSequenceOnMachines), PopulationMember(secondChildSequenceOnMachines)

if __name__ == "__main__":
    # shouldLog = False
    inputPath = 'ptsz-i3-prawa/inf127147/50.txt'
    tasks = loadData(inputPath)
    log(True, len(tasks))

    # tasksWithMissing = tasks[:]
    # tasksWithMissing.pop(1)

    # log(True, type(tasksWithMissing))

    # tasksOnMachines = []
    # tasksOnMachines.append(tasksWithMissing[0:3])
    # tasksOnMachines.append(tasksWithMissing[3:7])
    # tasksOnMachines.append(tasksWithMissing[7:9])
    # tasksOnMachines.append(tasksWithMissing[9:20])

    # log(True, tasksOnMachines)
    # tasksOnMachines = fixSequenceOfTasksOnMachines(tasksOnMachines, False)
    
    # log(True, tasksOnMachines)

    # create first population
    listAlgorithm = ListAlgorithm(inputPath, False)
    listAlgorithm.algorithm()
    listAlgorithmSolution = listAlgorithm.jobsOnMachines
    print(listAlgorithmSolution)

    # convert to proper task representation
    sequenceOfTasksOnMachinesListAlgorithmSolution = [[], [], [], []]
    for i in range(4):
        sequenceOfTasksOnMachinesListAlgorithmSolution[i] = [Task(id, tasks[id-1].processingTime, tasks[id-1].readyTime, tasks[id-1].dueDate) for id in listAlgorithmSolution[i]] 
        
    print(sequenceOfTasksOnMachinesListAlgorithmSolution)

    
    population[0] = PopulationMember(sequenceOfTasksOnMachinesListAlgorithmSolution)
    print(len(population))
    print(population[0])


    population[1] = mutate(population[0])
    print(population)
    
    population[2], population[3] = crossover(population[0], population[1])
    print(population)

