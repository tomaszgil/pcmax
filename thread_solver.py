from sys import path
from time import time
from threading import Thread
path.append('lib')

#import custom classes
from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from pcmaxgenetic import PCMaxGenetic, OptimumFoundException
from filereader import FileReader
from instancegenerator import InstanceGenerator


startTime = time()

# files = [
#   'instances/m50n1000.txt', 'instances/m25.txt', 'instances/regular-instance',
#   'instances/instance.txt', 'instances/test.txt', 'instances/optimum-instance',
#   'instances/m50.txt'
#   ]
files = ['instances/m50n1000.txt', 'instances/m25.txt', 'instances/m50.txt']

def processGenetic(fileName):
  results = {}
  reader = FileReader(fileName)
  procNum = reader.readline()
  taskNum = reader.readline()
  t1 = time()
  execTimes = [reader.readline() for _ in range(taskNum)]

  times = []

  genetics = [PCMaxGenetic(execTimes, procNum) for _ in range(10)]
  for genetic in genetics:
    try:
      data, cmax = genetic.solve(100000, 0.1)
      times.append(cmax)
    except OptimumFoundException, e:
      times.append(e.cmax)
      break

  print times

  results['Optimum'] = reader.readline() or 'unknown'
  _, results['LPT'] = PCMaxLPT(execTimes, procNum).solve()
  _, results['Rotate'] = PCMaxRotate(execTimes, procNum).solve()
  results['Genetic'] = min(times)
  t2 = time()
  print fileName + '   ' + str(t2-t1) + ":\n      ", results

threads = []
for fileName in files:
  #processGenetic(fileName)
  t = Thread(target=processGenetic, args=(fileName,))
  t.deamon = True
  threads.append(t)
  t.start()

for thread in threads:
  thread.join()
  

endTime = time()

print 'execTime: ' + str(endTime - startTime)
