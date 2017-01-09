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
# files = ['instances/m50n1000.txt', 'instances/m25.txt', 'instances/m50.txt']

for fileName in files:
  results = {}
  reader = FileReader(fileName)
  procNum = reader.readline()
  taskNum = reader.readline()
  
  execTimes = [reader.readline() for _ in range(taskNum)]
  
  times = []
  
  genetics = [PCMaxGenetic(execTimes, procNum) for _ in range(10)]
  for genetic in genetics:
    data, cmax = genetic.solve(100000, 0.1)
    times.append(cmax)
  print times
  
  results['Optimum'] = reader.readline() or 'unknown'
  _, results['LPT'] = PCMaxLPT(execTimes, procNum).solve()
  _, results['Rotate'] = PCMaxRotate(execTimes, procNum).solve()
  results['Genetic'] = min(times)
  
  print fileName + ":\n      ", results

endTime = time()

print 'execTime: ' + str(endTime - startTime)
