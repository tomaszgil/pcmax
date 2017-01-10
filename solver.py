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

for fileName in files:
  results = GeneticSolver({
    'fileName': fileName,
    'instNum': 10,
    'iterNum': 100000,
    'mutationsCoeff': 0.1
  }).solve()
  print fileName + ":\n      ", results

endTime = time()

print 'execTime: ' + str(endTime - startTime)
