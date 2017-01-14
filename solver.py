#append path to access lib classes
from sys import path
from time import time
path.append('lib')

from glob import glob

#import genetic solution wrapper
from geneticsolver import GeneticSolver


startTime = time()

files = ['instances/testing/m10n1000', 'instances/testing/m10n2000', 'instances/testing/m10n3000',
    'instances/testing/m10n4000', 'instances/testing/m10n5000', 'instances/testing/m10n6000',
    'instances/testing/m10n7000', 'instances/testing/m10n8000', 'instances/testing/m10n9000',
    'instances/testing/m10n10000', 'instances/testing/m10n1000', 'instances/testing/m15n1000',
    'instances/testing/m20n1000', 'instances/testing/m25n1000', 'instances/testing/m30n1000',
    'instances/testing/m35n1000', 'instances/testing/m40n1000', 'instances/testing/m45n1000',
    'instances/testing/m50n1000', 'instances/testing/m55n1000']

params = [
  { 'instNum': 1, 'iterNum': 1000, 'mutIter': 100, 'normIter': 2 }
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 50, 'normIter': 2 },
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 4 },
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 50, 'normIter': 4 },
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 8 },
  # { 'instNum': 10, 'iterNum': 100000, 'mutIter': 50, 'normIter': 8 }
]

# factory for creating all combination between files and params
geneticParams = []
for file in files:
  for param in params:
    geneticParams.append(dict(param, **{'fileName':file}))

# solving all problems from geneticParams

header = ['Rotate', 'GeneticAvg', 'LPT', 'GeneticIter', 'GeneticMedian', 'FileName', 'Genetic', 'Optimum']
f = open('results.csv', 'w')
f.write(','.join(header) + "\n")

for geneticParam in geneticParams:
  results = GeneticSolver(geneticParam).solve()
  #print geneticParam['fileName'] + ' mut: ' + str(geneticParam['mutIter']) + ' norm: ' + str(geneticParam['normIter']) + ":\n      ", results
  
  line = []
  for k in header:
    line.append(str(results[k]))
  f.write(','.join(line) + "\n")

endTime = time()

print 'execTime: ' + str(endTime - startTime)
