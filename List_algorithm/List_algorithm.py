import numpy as np
import sys

class ListAlgorithm:
    def __init__(self, inputPath, log = False):
        self.jobsArray = self.readData(inputPath)
        self.logFlag = log
        self.machineTimesNow = [0 for _ in range(4)]
        self.jobsOnMachines = [[] for _ in range(4)]

    def readData(self, inputPath):
        array = []
        with open(inputPath, 'r') as file:
            N = int(file.readline())
            for i in range (0, N):
                one = file.readline().split() + [i]
                array.append(one)
        #jobsArray[i]: 
        #0 is processing time
        #1 is ready time
        #2 is due date
        #3 is id
        jobsArray = np.array(array).astype(int)
        return jobsArray

    def sortJobsByReadyTimesAndDueDates(self):
        if(self.logFlag): print("before sorting: {}".format(self.jobsArray))
        print(type(self.jobsArray))
        self.jobsArray = sorted(self.jobsArray, key= lambda x : 10 * x[1] + x[2])
        self.jobsArray = np.asarray(self.jobsArray)
        if(self.logFlag): print("after sorting: {}".format(self.jobsArray))
        print(type(self.jobsArray))


    def getJobWithLowestReadyTime(self):
        index_min = np.argmin(self.jobsArray[:, 1])
        if(self.logFlag): print("Index of job with lowest ready time: {}, ri = {}".format(index_min, self.jobsArray[index_min]))
        return index_min

    def getMachineWithLowestTime(self):
        return np.argmin(self.machineTimesNow)

    def algorithm(self):
        self.sortJobsByReadyTimesAndDueDates()
        
        for job in self.jobsArray:
            machineIndex = self.getMachineWithLowestTime()
            self.machineTimesNow[machineIndex] = self.machineTimesNow[machineIndex] + job[0]
            self.jobsOnMachines[machineIndex].append(job[3])

    def saveToFile(self, outputPath):
        with open(outputPath, 'w+') as file:
            for i in range(4):
                file.write(self.jobsOnMachines[i])

if __name__ == "__main__":
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    listAlgorithm = ListAlgorithm(inputPath, True)
    listAlgorithm.algorithm()



# get job with lowest ready time
# put it on machine where time lowest
# check if it breaks any due dates
# if so, try on another machine

# 1. get a job that can be run
# 2. if more than one such job, get one with shortest due date