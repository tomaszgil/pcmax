from pcmaxgreedy import PCMaxGreedy
from datastruct import DataStruct
from instancegenerator import InstanceGenerator
from normalizer import Normalizer
fileName = "../instances/regular-instance"

reader = DataStruct(fileName)
procNum = reader.readline()
taskNum = reader.readline()

execTimes = []
for _ in range(taskNum):
  execTimes.append(reader.readline())

optimumCmax = reader.readline()

algorithm = PCMaxGreedy(execTimes, procNum)
data, cmax = algorithm.solve()

#normalizer = Normalizer(data)
#normalizedData, normalizedCmax = normalizer.swap(1000)

print "CMax:"
print cmax #, normalizedCmax
if optimumCmax:
    print "Expected:"
    print optimumCmax
