from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from pcmaxgenetic import PCMaxGenetic
from normalizer import Normalizer
from datastruct import DataStruct
from instancegenerator import InstanceGenerator
fileName = "../instances/m50n1000.txt"

reader = DataStruct(fileName)
procNum = reader.readline()
taskNum = reader.readline()

execTimes = []
for _ in range(taskNum):
  execTimes.append(reader.readline())

optimumCmax = reader.readline()

algorithm = PCMaxLPT(execTimes, procNum)
data, cmax = algorithm.solve()


results = []
#todo: Use wrapper for this
for i in range(10):
  genetics = [PCMaxGenetic(execTimes, procNum) for _ in range(10)]
  data = [genetic.solve(20000) for genetic in genetics]
  results.append(data[1][-1])
  print results

print "CMax: <LPT, genetic>"
print cmax, min(results)
if optimumCmax:
    print "Expected:"
    print optimumCmax
