from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from pcmaxgenetic import PCMaxGenetic
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

algorithm = PCMaxLPT(execTimes, procNum)
data, cmax = algorithm.solve()

genetic = PCMaxGenetic(execTimes, procNum)
normalizedData, normalizedCmax = genetic.solve(1000000)

print "CMax:"
print cmax, normalizedCmax
if optimumCmax:
    print "Expected:"
    print optimumCmax
