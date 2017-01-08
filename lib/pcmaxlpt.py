class PCMaxLPT:
  def __init__(self, execTimes, procNum):
    self.execTimes = execTimes
    self.procNum = procNum

  def solve(self):
    sortedExecTimes = sorted(self.execTimes, reverse=True)
    processorsData = [[] for _ in range(self.procNum)]

    for execTime in sortedExecTimes:
      processorsTime = [sum(processor) for processor in processorsData]
      earliestAvailableProcessor = processorsTime.index(min(processorsTime))
      processorsData[earliestAvailableProcessor].append(execTime)

    cmax = max([sum(processor) for processor in processorsData])
    return processorsData, cmax
