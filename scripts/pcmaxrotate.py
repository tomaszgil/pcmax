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
    times = sorted(self.execTimes, reverse=True)
    target = float(sum(times)) / self.procNum
    processorsData = [[] for i in range(self.procNum)]
    
    rotateCounter = RotateCounter(0, self.procNum - 1)
    for i in times:
      processorsData[rotateCounter.counter].append(i)
      rotateCounter.increment()

    print processorsData
    print times, self.procNum, target


x = PCMaxRotate([6,7,8,10,4,3,2],4)
x.solve()

