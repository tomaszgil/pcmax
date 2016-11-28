from pcmaxgreedy import PCMaxGreedy
from datastruct import DataStruct
from instancegenerator import InstanceGenerator
fileName = "../instances/m50n1000.txt"

#generator = InstanceGenerator(50, 1000, 1000)
#generator.generateInstance()
#generator.save("test.txt")

reader = DataStruct(fileName)
procNum = reader.readline()
taskNum = reader.readline()

execTimes = []
for _ in range(taskNum):
  execTimes.append(reader.readline())

reader.readline()
cmax = reader.readline()

algorithm = PCMaxGreedy(execTimes, procNum)
data, cmax = algorithm.solve()
print("Result: \n")
print(cmax)
