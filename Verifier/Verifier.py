import numpy as np
import subprocess
import sys
import time

def verify(inputPath, pathToSolution):
    array = []
    with open(inputPath, 'r') as file:
        N = int(file.readline())
        for _ in range (0, N):
            array.append(file.readline().split())

    jobsArray = np.array(array).astype(int)
    # print(jobsArray)

    isTrue = False
    computedTardiness = 0

    with open(pathToSolution, 'r') as file:
        tardiness = int(file.readline())
        print(tardiness)
        if (tardiness == 0):
            isTrue = True

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
                    computedTardiness = computedTardiness + abs(potentialTardiness)

        if (computedTardiness == tardiness): isTrue = True
    return computedTardiness, isTrue

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
        computedTardiness, isOk = verify(sys.argv[1], sys.argv[2])
        print(str(computedTardiness), str(isOk))
        exit()

    if (len(sys.argv) == 4):
        print("Running with 3 parameters: path to instances, algorithm and path to output file to check.")
        
        # 1 - input
        # 2 - algorytm
        # 3 - output
        # run algorithm

        timeBefore = time.time()
        subprocess.call([sys.argv[2], sys.argv[1], sys.argv[3]])
        timeAfter = time.time()

        time = timeAfter - timeBefore
        computedTardiness, isOk = verify(sys.argv[1], sys.argv[3])
        print(str(computedTardiness), str(isOk), str(time))

        with open("wynikis.txt", 'w+') as file:
            file.write(str(sys.argv[1]), str(isOk), str(time))