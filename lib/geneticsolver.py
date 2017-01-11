#import custom classes
from pcmaxlpt import PCMaxLPT
from pcmaxrotate import PCMaxRotate
from pcmaxgenetic import PCMaxGenetic, OptimumFoundException
from filereader import FileReader
from instancegenerator import InstanceGenerator

from numpy import median

class GeneticSolver:
  def __init__(self, data):
    self.fileName = data['fileName']
    self.instNum = data['instNum']
    self.iterNum = data['iterNum']
    self.normIter = data['normIter']
    self.mutIter = data['mutIter']

  def solve(self):
    results = {}
    reader = FileReader(self.fileName)
    procNum = reader.readline()
    taskNum = reader.readline()

    execTimes = [reader.readline() for _ in range(taskNum)]

    times = []

    genetics = [PCMaxGenetic(execTimes, procNum) for _ in range(self.instNum)]
    for genetic in genetics:
      try:
        _, cmax = genetic.solve(self.iterNum, self.normIter, self.mutIter)
        times.append(cmax)
      except OptimumFoundException, e:
        times.append(e.cmax)
        break

    results['Optimum'] = reader.readline() or 'unknown'
    _, results['LPT'] = PCMaxLPT(execTimes, procNum).solve()
    _, results['Rotate'] = PCMaxRotate(execTimes, procNum).solve()
    results['Genetic'] = min(times)
    results['GeneticAvg'] = float(sum(times))/len(times)
    results['GeneticMedian'] = median(times)
    results['GeneticIter'] = len(times)


    return results
