from pcmaxgreedy import PCMaxGreedy
from normalizer import Normalizer
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

normalizer = Normalizer(data)
normalizedData, normalizedCmax = normalizer.swap(1000)

print "CMax:"
print cmax, normalizedCmax
if optimumCmax:
    print "Expected:"
    print optimumCmax
