class PCMaxDummy:
  def __init__(self, execTimes, procNum):
    self.execTimes = execTimes
    self.procNum = procNum

  def solve(self):
    processorsData = [[] for _ in range(self.procNum)]
    i = 0

    for execTime in self.execTimes:
      processorsData[i % self.procNum].append(execTime)
      i += 1

    cmax = max([sum(processor) for processor in processorsData])
    return processorsData, cmax
