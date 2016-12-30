from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from random import randint

class PCMaxGenetic:
    def __init__(self, execTimes, procNum):
        self.execTimes = execTimes
        self.procNum = procNum
        self.processorsData = []
        self.processorsTimes = []

    def solve(self, repetitions, mutationsCoeff = 0.1):
        self.processorsData = self.findBestGreedySolution()
        self.processorsTimes = [sum(processor) for processor in self.processorsData]
        for i in range(repetitions):
            if i % int(1 / mutationsCoeff) == 0:
                self.mutate()
            else:
                self.swapTasksBetweenProcessors()
                # todo: swap tasks between more than 2 processors

        return self.processorsData, max(self.processorsTimes)

    def findBestGreedySolution(self):
        greedyAlgorithms = []
        greedyAlgorithms.append(PCMaxLPT(self.execTimes, self.procNum))
        greedyAlgorithms.append(PCMaxRotate(self.execTimes, self.procNum))
        bestCMax = 0
        bestData = []

        for algorithm in greedyAlgorithms:
            data, cmax = algorithm.solve()
            if cmax < bestCMax or not bestData:
                bestData = data

        return bestData

    def mutate(self):
        idxOfLongest = self.processorsTimes.index(max(self.processorsTimes))
        idxOfRandom = randint(0, len(self.processorsData)-1)
        idxTaskInLongest = randint(0, len(self.processorsData[idxOfLongest])-1)
        idxTaskInRandom = randint(0, len(self.processorsData[idxOfRandom])-1)

        currentCMax = max(self.processorsTimes)
        self.processorsData[idxOfLongest][idxTaskInLongest], self.processorsData[idxOfRandom][idxTaskInRandom] = self.processorsData[idxOfRandom][idxTaskInRandom], self.processorsData[idxOfLongest][idxTaskInLongest]
        self.processorsTimes[idxOfLongest] += (self.processorsData[idxOfRandom][idxTaskInRandom] - self.processorsData[idxOfLongest][idxTaskInLongest])
        self.processorsTimes[idxOfRandom] += (self.processorsData[idxOfLongest][idxTaskInLongest] - self.processorsData[idxOfRandom][idxTaskInRandom])
        if currentCMax < max(self.processorsTimes):
            self.processorsData[idxOfLongest][idxTaskInLongest], self.processorsData[idxOfRandom][idxTaskInRandom] = self.processorsData[idxOfRandom][idxTaskInRandom], self.processorsData[idxOfLongest][idxTaskInLongest]
            self.processorsTimes[idxOfLongest] += (self.processorsData[idxOfLongest][idxTaskInLongest] - self.processorsData[idxOfRandom][idxTaskInRandom])
            self.processorsTimes[idxOfRandom] += (self.processorsData[idxOfRandom][idxTaskInRandom] - self.processorsData[idxOfLongest][idxTaskInLongest])

    def swapTasksBetweenProcessors(self):
        idxOfShortest = self.processorsTimes.index(min(self.processorsTimes))
        idxOfLongest = self.processorsTimes.index(max(self.processorsTimes))
        processorsConcatenated = self.processorsData[idxOfShortest] + self.processorsData[idxOfLongest]
        algorithm = PCMaxLPT(processorsConcatenated, 2)

        newData, cmax = algorithm.solve()
        self.processorsData[idxOfShortest] = newData[0]
        self.processorsData[idxOfLongest] = newData[1]
        self.processorsTimes[idxOfShortest] = sum(self.processorsData[idxOfShortest])
        self.processorsTimes[idxOfLongest] = sum(self.processorsData[idxOfLongest])

    def __del__(self):
        pass


genetic = PCMaxGenetic([2,5,2,5,2,10,3,4,1,5,2], 4)
data, cmax = genetic.solve(10)
