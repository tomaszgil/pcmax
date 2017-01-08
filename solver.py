from sys import path
from time import time
path.append('lib')

#import custom classes
from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from pcmaxgenetic import PCMaxGenetic
from filereader import FileReader
from instancegenerator import InstanceGenerator


startTime = time()

files = [
  'instances/m50n1000.txt', 'instances/m25.txt', 'instances/regular-instance',
  'instances/instance.txt', 'instances/test.txt', 'instances/optimum-instance',
  'instances/m50.txt'
  ]

for fileName in files:
  results = {}
  reader = FileReader(fileName)
  procNum = reader.readline()
  taskNum = reader.readline()
  
  execTimes = [reader.readline() for _ in range(taskNum)]
  
  times = []
  for _ in range(10):
    genetics = [PCMaxGenetic(execTimes, procNum) for _ in range(10)]
    data = [genetic.solve(10000, 0.1) for genetic in genetics]
    times.append(data[1][-1])
    
  results['Optimum'] = reader.readline() or 'unknown'
  _, results['LPT'] = PCMaxLPT(execTimes, procNum).solve()
  _, results['Rotate'] = PCMaxRotate(execTimes, procNum).solve()
  results['Genetic'] = min(times)
  
  print fileName + ":\n      ", results

endTime = time()

print 'execTime: ' + str(endTime - startTime)
