from random import randint, shuffle
from pcmaxlpt import PCMaxLPT


class InstanceGenerator:
    def __init__(self, procNum, taskNum, minExecTime, maxExecTime):
        self.procNum = procNum
        self.taskNum = taskNum
        self.minExecTime = minExecTime if minExecTime > 0 else 1
        self.maxExecTime = maxExecTime if maxExecTime > 0 else 1
        self.tasks = []
        self.cmax = 0

    def generateInstance(self):
        self.tasks = [randint(1, self.maxExecTime) for i in range(self.taskNum)]
        shuffle(self.tasks)
        self.taskNum = len(self.tasks)

    def generateOptimumInstance(self):
        randomTaskNum = self.taskNum - self.procNum
        randomTasks = [randint(1, self.maxExecTime) for i in range(randomTaskNum)]
        algorithm = PCMaxLPT(randomTasks, self.procNum)
        processorsData, self.cmax = algorithm.solve()
        self.tasks = []
        for processor in processorsData:
            remainingTime = self.cmax - sum(processor)
            if remainingTime > 0:
                self.tasks.append(remainingTime)
            self.tasks += processor
        shuffle(self.tasks)
        self.taskNum = len(self.tasks)

    # Saving to file in instances directory
    # Consecutively: number of processors, number of tasks, execution times, CMax value if known
    def save(self, fileName):
        file = open("../instances/" + fileName, 'w')
        file.write(str(self.procNum) + '\n')
        file.write(str(self.taskNum) + '\n')
        for taskTime in self.tasks:
            file.write(str(taskTime) + '\n')
        if self.cmax:
            file.write(str(self.cmax) + '\n')
        file.close()
