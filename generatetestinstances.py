from sys import path
path.append('lib')

from instancegenerator import InstanceGenerator
from instancegenerator import PCMaxLPT


procNum = 10
deltaProc = 5
taskNum = 1000
deltaTask = 1000
minExecTime = 1
maxExecTime = 1000
expectedDiff = 1

g = InstanceGenerator(procNum, taskNum, minExecTime, maxExecTime)

# instances with changing m
for i in range(10):
  diff = False
  while not diff:
    print i
    g.generateOptimumInstance()
    lpt = PCMaxLPT(g.tasks, g.procNum)
    _, lptResult = lpt.solve()
    diff = lptResult - g.cmax >= expectedDiff
    if not diff:
      g.taskNum = taskNum
      g.reset()
  g.save("testing/m" + str(g.procNum) + "n" + str(taskNum))
  g.taskNum = taskNum
  g.procNum += deltaProc

g.setParameters(procNum, taskNum, minExecTime, maxExecTime)

# instances with changing n
for i in range(10):
  diff = False
  while not diff:
    print i
    g.generateOptimumInstance()
    lpt = PCMaxLPT(g.tasks, g.procNum)
    _, lptResult = lpt.solve()
    diff = lptResult - g.cmax >= expectedDiff
    if not diff:
      g.taskNum = taskNum + i * deltaTask
      g.reset()
  g.save("testing/m" + str(g.procNum) + "n" + str(taskNum + i * deltaTask))
  g.taskNum = taskNum + (i+1) * deltaTask
