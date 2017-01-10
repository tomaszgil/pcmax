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
geneticParams = [
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.1 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.2 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.3 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.4 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.5 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.6 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.7 },
  { 'instNum': 10, 'iterNum': 100000, 'mutationsCoeff': 0.8 },
]

for fileName in files:
  for geneticParam in geneticParams:
    geneticParam['fileName'] = fileName
    results = GeneticSolver(geneticParam).solve()
    print fileName + ' ' + str(geneticParam['mutationsCoeff']) + ":\n      ", results

endTime = time()

print 'execTime: ' + str(endTime - startTime)
