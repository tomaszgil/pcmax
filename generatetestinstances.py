from sys import path
path.append('lib')

from instancegenerator import InstanceGenerator

procNum = 10
deltaProc = 5
taskNum = 1000
deltaTask = 1000
minExecTime = 1
maxExecTime = 1000

g = InstanceGenerator(procNum, taskNum, minExecTime, maxExecTime)

# instances with changing n
for _ in range(10):
  g.generateOptimumInstance()
  g.save("testing/m" + str(g.procNum) + "n" + str(g.taskNum))
  g.procNum += deltaProc

g.setParameters(procNum, taskNum, minExecTime, maxExecTime)

# instances with changing m
for _ in range(10):
  g.generateOptimumInstance()
  g.save("testing/m" + str(g.procNum) + "n" + str(g.taskNum))
  g.taskNum += deltaTask
