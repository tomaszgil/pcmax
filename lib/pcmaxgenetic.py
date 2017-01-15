from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from random import randint

class OptimumFoundException(Exception):
  def __init__(self, result):
    self.cmax = result

class PCMaxGenetic:
  def __init__(self, execTimes, procNum):
    self.execTimes = execTimes
    self.procNum = procNum
    self.procData = []
    self.procTimes = []
    self.bestData = []
    self.cmax = 0

  def solve(self, repetitions, normIter, mutIter):
    self.procData = self.findBestGreedySolution()
    self.procTimes = [sum(proc) for proc in self.procData]
    self.cmax = max(self.procTimes)
    for i in range(repetitions):
      if i % mutIter == 0:
        self.mutate()
      elif i % normIter == 0:
        self.normalize()
      else:
        try:
          self.swapTasksBetweenProc()
        except OptimumFoundException:
          raise

    return self.bestData, self.cmax

  def normalize(self):
    l = self.procTimes.index(max(self.procTimes)) # index of longest proc
    r = randint(0, len(self.procData) - 1) # index of random proc
    if l != r:
      tl = randint(0, len(self.procData[l]) - 1) # index of random task in longest proc
      tr = randint(0, len(self.procData[r]) - 1) # index of random task in random proc

      currentCMax = max(self.procTimes)
      self.procData[l][tl], self.procData[r][tr] = self.procData[r][tr], self.procData[l][tl]
      self.procTimes[l] = sum(self.procData[l])
      self.procTimes[r] = sum(self.procData[r])
      if currentCMax < max(self.procTimes):
        self.procData[l][tl], self.procData[r][tr] = self.procData[r][tr], self.procData[l][tl]
        self.procTimes[l] = sum(self.procData[l])
        self.procTimes[r] = sum(self.procData[r])

    self.saveResult()

  def swapTasksBetweenProc(self):
    s = self.procTimes.index(min(self.procTimes)) # index of shortest proc
    l = self.procTimes.index(max(self.procTimes)) # index of longest proc

    if self.procTimes[l] - self.procTimes[s] <= 1:
      raise OptimumFoundException(self.procTimes[l])

    # try to improve score with LPT for 2 proc
    procConcatenated = self.procData[s] + self.procData[l]
    algorithm = PCMaxLPT(procConcatenated, 2)
    newData, cmax = algorithm.solve()

    # if sortest and longest cannot be improved by LPT, try LPT for 3 proc
    if self.procData[s] == newData[0] or self.procData[l] == newData[1]:
      r = randint(0, self.procNum - 1)
      if r != l and r != s:
        procConcatenated = self.procData[s] + self.procData[l] + self.procData[r]
        algorithm = PCMaxLPT(procConcatenated, 3)
        newData, newCmax = algorithm.solve()

        # check if cmax is better
        if newCmax <= cmax:
          self.procData[s] = newData[0]
          self.procData[l] = newData[1]
          self.procData[r] = newData[2]
          self.procTimes[s] = sum(self.procData[s])
          self.procTimes[l] = sum(self.procData[l])
          self.procTimes[r] = sum(self.procData[r])
    else:
      self.procData[s] = newData[0]
      self.procData[l] = newData[1]
      self.procTimes[s] = sum(self.procData[s])
      self.procTimes[l] = sum(self.procData[l])

    self.saveResult()

  def mutate(self):
    x = randint(0, self.procNum - 1)
    y = randint(0, self.procNum - 1)
    if x != y:
      index1 = randint(0, len(self.procData[x])-1)
      index2 = randint(0, len(self.procData[y])-1)
      t1 = self.procData[x][index1]
      t2 = self.procData[y][index2]
      self.procData[x][index1] = t2
      self.procData[y][index2] = t1
      self.procTimes[x] = sum(self.procData[x])
      self.procTimes[y] = sum(self.procData[y])

    self.saveResult()

  def saveResult(self):
    if max(self.procTimes) < self.cmax:
      self.bestData = self.procData
      self.cmax = max(self.procTimes)

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

  def __del__(self):
    pass
