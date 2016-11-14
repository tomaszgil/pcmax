from random import randint
from pcmaxgreedy import PCMaxGreedy


class InstanceGenerator:
    def __init__(self, procNum, taskNum, maxExecTime):
        self.procNum = procNum
        self.taskNum = taskNum
        self.maxExecTime = maxExecTime
        self.tasks = []
        self.finalTaskNum = 0
        self.cmax = 0

    def generateInstance(self):
        generatedTaskNum = int(self.taskNum * 0.9)
        execTimes = [randint(1, self.maxExecTime) for i in range(generatedTaskNum)]
        pcmaxAlgorithm = PCMaxGreedy(execTimes, self.procNum);
        processorsData, self.cmax = pcmaxAlgorithm.solve()

        for processor in processorsData:
            remainingTime = sum(processor) - self.cmax
            if remainingTime > 0:
                processor.append(remainingTime)
            self.tasks += processor

        self.finalTaskNum = len(self.tasks)

    # Saving to file in instances dir.
    # Consecutively: number of processors, number of tasks, execution times, CMax value 
    def save(self, fileName):
        file = open("../instances/" + fileName, 'w')

        file.write(str(self.procNum) + '\n')
        file.write(str(self.finalTaskNum) + '\n')
        for taskTime in self.tasks:
            file.write(str(taskTime) + '\n')
        file.write('\nCMax: ' + str(self.cmax) + '\n')

        file.close()


generator = InstanceGenerator(5, 20, 15)
generator.generateInstance()
generator.save("testinstance")
