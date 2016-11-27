from pcmaxgreedy import PCMaxGreedy
from datastruct import DataStruct
fileName = "../instances/testinstance"

reader = DataStruct(fileName)
procNum = reader.readline()
taskNum = reader.readline()

execTimes = []
for _ in range(taskNum):
  execTimes.append(reader.readline())

reader.readline()
cmax = reader.readline()

algorithm = PCMaxGreedy(execTimes, procNum)
print("Result: \n", algorithm.solve())
print("Expected CMax: ", cmax)
