from random import randint
from copy import deepcopy

class Normalizer:
  def __init__(self, processorsData):
    self.procNum = len(processorsData)
    #using list comprehension for perfomance issues
    self.processorsData = [[singleData,sum(singleData)] for singleData in processorsData]
    self.bestData = [[singleData,sum(singleData)] for singleData in processorsData]

  def swap(self, n):
    while(n):
      data = self.processorsData
      first, second = randint(0, len(data)-1), randint(0, len(data)-1)
      if first != second:
        if data[first][1] > data[second][1]:
          firstEl, secondEl = data[first], data[second]
        else:
          firstEl, secondEl = data[second], data[first]
        diff = firstEl[1] - secondEl[1]
        if len(firstEl[0]) > 1:
          el = firstEl[0].pop()
          firstEl[1] -= el
          secondEl[1] += el
          secondEl[0].append(el) #to_sorted
          secondEl[0].sort(reverse = True)
          data[first], data[second] = firstEl, secondEl
        self.processorsData = data
      n -= 1
      if max([x[-1] for x in data]) < max([x[-1] for x in self.bestData]):
        self.bestData = deepcopy(data)

    cmax = max([processor[1] for processor in self.bestData])
    return self.bestData, cmax

#deepcopying need fix -> performance and self.processorsData
#arrays should be mapped using list comprehension
