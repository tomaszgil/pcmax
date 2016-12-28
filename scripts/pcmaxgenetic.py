from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate

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
        pass

    def swapTasksBetweenProcessors(self):
        pass

    def __del__(self):
        pass


genetic = PCMaxGenetic([2,5,2,5,2,20,3,4,1,5,2], 4)
genetic.solve(50)
