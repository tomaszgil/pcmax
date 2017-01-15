class RotateCounter:
  def __init__(self, bottomBorder, topBorder):
    self.x = bottomBorder
    self.y = topBorder
    self.state = 'asc'
    self.counter = bottomBorder

  def increment(self):
    if self.state == 'asc':
      self.counter += 1
      if self.counter == self.y:
        self.state = 'asc_stop'

    elif self.state == 'desc':
      self.counter -= 1
      if self.counter == self.x:
        self.state = 'desc_stop'

    elif self.state == 'asc_stop':
      self.state = 'desc'

    elif self.state == 'desc_stop':
      self.state = 'asc'

    return(self.counter)



class PCMaxRotate:
  def __init__(self, execTimes, procNum):
    self.execTimes = execTimes
    self.procNum = procNum

  def solve(self):
    sortedExecTimes = sorted(self.execTimes, reverse=True)
    processorsData = [[] for i in range(self.procNum)]

    rotateCounter = RotateCounter(0, self.procNum - 1)
    for i in sortedExecTimes:
      processorsData[rotateCounter.counter].append(i)
      rotateCounter.increment()

    cmax = max([sum(processor) for processor in processorsData])
    return processorsData, cmax
