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
# factory pattern should be used here - create list of all files and geneticParams combination
params = [
  { 'instNum': 3, 'iterNum': 100000, 'mutationsCoeff': 100000, 'normIter': 1 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 2000, 'normIter': 2 }
  # { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 4000, 'normIter': 2 },
  # { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 8000, 'normIter': 2 },
]
geneticParams = {}
for file in files:
  for param in params:
    geneticParams = param.update({'fileName': file})

print geneticParams

for geneticParam in geneticParams:
  results = GeneticSolver(geneticParam).solve()
  print fileName + ' ' + str(geneticParam['mutationsCoeff']) + ":\n      ", results

endTime = time()

print 'execTime: ' + str(endTime - startTime)
