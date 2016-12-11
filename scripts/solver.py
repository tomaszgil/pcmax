from pcmaxgreedy import PCMaxGreedy
from datastruct import DataStruct
from instancegenerator import InstanceGenerator
fileName = "../instances/optimum-instance"

reader = DataStruct(fileName)
procNum = reader.readline()
taskNum = reader.readline()

execTimes = []
for _ in range(taskNum):
  execTimes.append(reader.readline())

optimumCmax = reader.readline()

algorithm = PCMaxGreedy(execTimes, procNum)
data, cmax = algorithm.solve()

print "CMax:"
print cmax
if optimumCmax:
    print "Expected:"
    print optimumCmax
