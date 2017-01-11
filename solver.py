#append path to access lib classes
from sys import path
from time import time
path.append('lib')

#import genetic solution wrapper
from geneticsolver import GeneticSolver


startTime = time()

# files = [
#   'instances/m50n1000.txt', 'instances/m25.txt', 'instances/regular-instance',
#   'instances/instance.txt', 'instances/test.txt', 'instances/optimum-instance',
#   'instances/m50.txt'
#   ]
files = ['instances/m50n1000.txt', 'instances/m25.txt', 'instances/m50.txt']

params = [
  { 'instNum': 3, 'iterNum': 1000, 'mutIter': 100000, 'normIter': 1 },
  { 'instNum': 10, 'iterNum': 1000, 'mutIter': 2000, 'normIter': 2 }
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 4000, 'normIter': 2 },
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 8000, 'normIter': 2 },
]

# factory for creating all combination between files and params
geneticParams = []
for file in files:
  for param in params:
    geneticParams.append(dict(param, **{'fileName':file}))

# solving all problems from geneticParams
for geneticParam in geneticParams:
  results = GeneticSolver(geneticParam).solve()
  print geneticParam['fileName'] + ' ' + str(geneticParam['mutIter']) + ":\n      ", results

endTime = time()

print 'execTime: ' + str(endTime - startTime)
