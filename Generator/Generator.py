import numpy as np
import sys

class Job:
    def __init__(self, N):
        self.numOfJobs = N

    def generateProcessingTime(self, min, max):
        self.processingTime = np.random.randint(min, max)
        return self.processingTime

    def generateReadyTime(self, sumOfProcessingTimes):
        self.readyTime = np.random.randint(0, sumOfProcessingTimes/4 * 0.25)
        return self.readyTime

    def generateDueDate(self, sumOfProcessingTimes):
        # sumOfProcessingTimes / 4
        self.dueDate = np.random.randint(self.readyTime + self.processingTime, 1.2 * (self.readyTime + self.processingTime))
        return self.dueDate

    def __str__(self):
        return str(self.processingTime) + " " + str(self.readyTime) + " " + str(self.dueDate)

class Generator:
    def __init__(self, N):
        self.min = N/50
        self.max = N*4
        self.numOfJobs = N
        self.sumOfProcessingTimes = 0

    def generateJobs(self):
        self.jobs = []
        for i in range(self.numOfJobs):
            job = Job(self.numOfJobs)
            self.sumOfProcessingTimes = self.sumOfProcessingTimes + job.generateProcessingTime(self.min, self.max)
            self.jobs.append(job)

        for job in self.jobs:
            job.generateReadyTime(self.sumOfProcessingTimes)
            job.generateDueDate(self.sumOfProcessingTimes)

        self.jobs = np.asarray(self.jobs)

    def castAsNpArray(self):
        array = []
        for job in self.jobs:
            array.append((job.processingTime, job.readyTime, job.dueDate))
        return np.array(array)

    def printJobs(self):
        for job in self.jobs:
            print(job)

    def saveToFile(self):
        with open('inf127147/{}.txt'.format(str(self.numOfJobs)), 'w+') as file:
            file.write(str(self.numOfJobs))
            file.write('\n')
            for job in self.jobs:
                file.write(str(job))
                file.write('\n')


def generateAllSizes():
    for n in range(50, 510, 50):
        generator = Generator(n)
        generator.generateJobs()
        generator.saveToFile()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        if (len(sys.argv) == 1):
            print("No number of jobs given. Generating all.")
            generateAllSizes()
        exit()
    
    N = int(sys.argv[1])
    generator = Generator(N)
    generator.generateJobs()
    generator.saveToFile()


    # generator.printJobs()
    print(generator.castAsNpArray())

