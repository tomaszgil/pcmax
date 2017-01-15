#append path to access lib classes
from sys import path
from time import time
from os import listdir
path.append('lib')

#import genetic solution wrapper
from geneticsolver import GeneticSolver


startTime = time()

files = ['instances/testing/' + str(f) for f in listdir('instances/testing')]

params = [
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 1 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 2 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 4 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 8 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 100, 'normIter': 16 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 64, 'normIter': 2 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 128, 'normIter': 2 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 256, 'normIter': 2 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 512, 'normIter': 2 },
  { 'instNum': 10, 'iterNum': 100000, 'mutIter': 1024, 'normIter': 2 },
]

# factory for creating all combination between files and params
geneticParams = []
for file in files:
  for param in params:
    geneticParams.append(dict(param, **{'fileName':file}))

# solving all problems from geneticParams

header = ['Rotate', 'GeneticAvg', 'LPT', 'GeneticIter', 'GeneticMedian', 'FileName', 'Genetic', 'Optimum', 'mutIter', 'normIter', 'iterNum']
f = open('results.csv', 'w')
f.write(','.join(header) + "\n")
print ','.join(header)

for geneticParam in geneticParams:
  results = GeneticSolver(geneticParam).solve()
  results['mutIter'] = geneticParam['mutIter']
  results['normIter'] = geneticParam['normIter']
  results['iterNum'] = geneticParam['iterNum']
  
  #print geneticParam['fileName'] + ' mut: ' + str(geneticParam['mutIter']) + ' norm: ' + str(geneticParam['normIter']) + ":\n      ", results
  
  line = []
  for k in header:
    line.append(str(results[k]))
  f.write(','.join(line) + "\n")
  print ','.join(line)

endTime = time()

print 'execTime: ' + str(endTime - startTime)
