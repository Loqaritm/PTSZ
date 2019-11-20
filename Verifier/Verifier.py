import numpy as np
import sys

def verify(inputPath, pathToSolution):
    array = []
    with open(inputPath, 'r') as file:
        N = int(file.readline())
        for _ in range (0, N):
            array.append(file.readline().split())

    jobsArray = np.array(array).astype(int)
    # print(jobsArray)

    with open(pathToSolution, 'r') as file:
        tardiness = int(file.readline())
        
        for _ in range (0,4):
            jobsOnMachine = np.array(file.readline().split()).astype(int)
            timeNow = 0

            for jobNumber in jobsOnMachine:
                #0 is processing time
                #1 is start time
                #2 is due date
                timeNow = max(jobsArray[jobNumber-1][1], timeNow) + jobsArray[jobNumber-1][0]

                potentialTardiness = jobsArray[jobNumber-1][2] - timeNow
                if (potentialTardiness < 0):
                    tardiness = tardiness + abs(potentialTardiness)
        
        return tardiness

def verifyAll(inputFolderPath, pathToSolutionFolder):
    tardinesses = ""
    for i in range(50, 510, 50):
        tardiness = verify(inputFolderPath + '/' + str(i) + '.txt', pathToSolutionFolder + '/' + str(i) + '.txt')
        print('for i =', i, 'tardiness =', tardiness)
        tardinesses = tardinesses + str(tardiness) + '\n'

    with open(inputFolderPath + 'tardinesses.txt', 'w+') as file:
        file.write(tardinesses)

if __name__ == "__main__":
    if (sys.argv[1] == 'all'):
        pathToAllInputs = sys.argv[2]
        pathToAllOutputs = sys.argv[3]
        # all
        # verify('inf132189', 'inf132189/dummy')
        verifyAll(pathToAllInputs, pathToAllOutputs)
        exit()

    if (len(sys.argv) == 3):
        print("Running with 2 parameters: path to instances and path to output file to check.")
        verify(sys.argv[1], sys.argv[2])
        exit()

    if (len(sys.argv) == 4):
        print("Running with 3 parameters: path to instances, algorithm and patch to output file to check.")
        exit()

