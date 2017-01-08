from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from random import randint

class PCMaxGenetic:
  def __init__(self, execTimes, procNum):
    self.logFile = open('logfile', 'w')
    self.execTimes = execTimes
    self.procNum = procNum
    self.processorsData = []
    self.processorsTimes = []

  def solve(self, repetitions, mutationsCoeff = 0.1):
    self.processorsData = self.findBestGreedySolution()
    self.processorsTimes = [sum(processor) for processor in self.processorsData]
    for i in range(repetitions):
      if i % int(1 / mutationsCoeff) == 0:
        self.logFile.write(str(self.processorsTimes))
        self.logFile.write("\n")
        self.mutate()
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
    l = self.processorsTimes.index(max(self.processorsTimes)) # index of longest processor
    r = randint(0, len(self.processorsData)-1) # index of random processor
    tl = randint(0, len(self.processorsData[l])-1) # index of random task in longest processor
    tr = randint(0, len(self.processorsData[r])-1) # index of random task in random processor

    currentCMax = max(self.processorsTimes)
    self.processorsData[l][tl], self.processorsData[r][tr] = self.processorsData[r][tr], self.processorsData[l][tl]
    self.processorsTimes[l] += (self.processorsData[r][tr] - self.processorsData[l][tl])
    self.processorsTimes[r] += (self.processorsData[l][tl] - self.processorsData[r][tr])
    if currentCMax < max(self.processorsTimes):
      self.processorsData[l][tl], self.processorsData[r][tr] = self.processorsData[r][tr], self.processorsData[l][tl]
      self.processorsTimes[l] += (self.processorsData[l][tl] - self.processorsData[r][tr])
      self.processorsTimes[r] += (self.processorsData[r][tr] - self.processorsData[l][tl])

  def swapTasksBetweenProcessors(self):
    s = self.processorsTimes.index(min(self.processorsTimes)) # index of shortest processor
    l = self.processorsTimes.index(max(self.processorsTimes)) # index of longest processor
    processorsConcatenated = self.processorsData[s] + self.processorsData[l]
    algorithm = PCMaxLPT(processorsConcatenated, 2)

    newData, cmax = algorithm.solve()
    self.processorsData[s] = newData[0]
    self.processorsData[l] = newData[1]
    self.processorsTimes[s] = sum(self.processorsData[s])
    self.processorsTimes[l] = sum(self.processorsData[l])

  def __del__(self):
    pass
