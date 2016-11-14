from random import randint
from copy import deepcopy

class Normalizer:
  def __init__(self, processorsData, procNum):
    self.procNum = procNum
    #using list comprehension for perfomance issues
    self.processorsData = [[singleData,sum(singleData)] for singleData in processorsData]
    self.bestData = [[singleData,sum(singleData)] for singleData in processorsData]

  def swap(self, n):
    while(n):
      data = self.processorsData
      first, second = randint(0, len(data)-1), randint(0, len(data)-1)
      if first != second:
        firstEl, secondEl = data[first], data[second]
        diff = firstEl[1] - secondEl[1]
        if diff > 0:
          if len(firstEl[0]) > 1:
            el = firstEl[0].pop()
            firstEl[1] -= el
            secondEl[1] += el
            secondEl[0].append(el) #to_sorted
            secondEl[0].sort(reverse = True) 
            data[first], data[second] = firstEl, secondEl
        elif diff < 0:
          if len(secondEl[0]) > 1:
            el = secondEl[0].pop()
            secondEl[1] -= el
            firstEl[1] += el
            firstEl[0].append(el) #to_sorted
            firstEl[0].sort(reverse = True)
            data[first], data[second] = firstEl, secondEl
        self.processorsData = data
      n -= 1
      if max([x[-1] for x in data]) < max([x[-1] for x in self.bestData]):
        self.bestData = deepcopy(data)
    return self.bestData

x = Normalizer([[52,62,12],[300,42,200],[300, 100, 210], [41, 40, 13]],4)

z = x.swap(10000)
print z

#deepcopying need fix -> performance and self.processorsData
#arrays should be mapped using list comprehension