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
                one = file.readline().split() + [i+1] + [0]
                array.append(one)
        #jobsArray[i]: 
        #0 is processing time
        #1 is ready time
        #2 is due date
        #3 is id
        #4 is tardiness of this job
        jobsArray = np.array(array).astype(int)
        return jobsArray

    def sortJobsByReadyTimesAndDueDates(self):
        if(self.logFlag):
            print("before sorting: {}".format(self.jobsArray))
            print(type(self.jobsArray))
        self.jobsArray = sorted(self.jobsArray, key= lambda x : 10 * x[1] + x[2])
        self.jobsArray = np.asarray(self.jobsArray)
        if(self.logFlag):
            print("after sorting: {}".format(self.jobsArray))
            print(type(self.jobsArray))


    def getJobWithLowestReadyTime(self):
        index_min = np.argmin(self.jobsArray[:, 1])
        if(self.logFlag): print("Index of job with lowest ready time: {}, ri = {}".format(index_min, self.jobsArray[index_min]))
        return index_min

    def getMachineWithLowestTime(self):
        return np.argmin(self.machineTimesNow)

    def getMachineWithClosestTimeToReadyTime(self, readyTime):
        print("dupa")
        print(self.machineTimesNow)
        lengths = [readyTime-x for x in self.machineTimesNow]
        print(lengths)
        return lengths.index(min(lengths))   

    def getProperMachine(self, job):
        machinesAfter = [max(x, job[1]) + job[0] for x in self.machineTimesNow]
        differences = [a - b for a, b in zip(machinesAfter, self.machineTimesNow)]
        
        summed = [4*a + b for a,b in zip(machinesAfter, differences)]
        return summed.index(min(summed))

    def algorithm(self):
        self.sortJobsByReadyTimesAndDueDates()
        self.tardinessForAll = 0
        
        for job in self.jobsArray:
            # machineIndex = self.getMachineWithLowestTime()
            # machineIndex = self.getMachineWithClosestTimeToReadyTime(job[1])
            machineIndex = self.getProperMachine(job)
            self.machineTimesNow[machineIndex] = max(self.machineTimesNow[machineIndex], job[1]) + job[0]
            self.jobsOnMachines[machineIndex].append(job[3])

            # set tardiness
            job[4] = max(0, self.machineTimesNow[machineIndex] - job[2])
            self.tardinessForAll = self.tardinessForAll + job[4]

    def saveToFile(self, outputPath):
        with open(outputPath, 'w+') as file:
            file.write(str(self.tardinessForAll))
            for jobsOnMachine in self.jobsOnMachines:
                file.write('\n')
                for jobID in jobsOnMachine:
                    file.write(str(jobID) + ' ')
                
                    

if __name__ == "__main__":
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    listAlgorithm = ListAlgorithm(inputPath, False)
    listAlgorithm.algorithm()
    print(listAlgorithm.tardinessForAll)
    # for machine in listAlgorithm.jobsOnMachines:
        # print(machine)
    
    listAlgorithm.saveToFile(outputPath)



# get job with lowest ready time
# put it on machine where time lowest
# check if it breaks any due dates
# if so, try on another machine

# 1. get a job that can be run
# 2. if more than one such job, get one with shortest due date