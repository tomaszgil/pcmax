from random import randint
from copy import deepcopy

class Normalizer:
  def __init__(self, processorsData, procNum):
    self.procNum = procNum
    self.processorsData = [[singleData,sum(singleData)] for singleData in processorsData]
    self.bestData = deepcopy(self.processorsData)

  def swap(self, x, n):
    while(n):
      data = self.processorsData
      first, secound = randint(0, len(data)-1), randint(0, len(data)-1)
      if first != secound:
        firstEl, secoundEl = data[first], data[secound]
        diff = firstEl[1] - secoundEl[1]
        if diff > x:
          if len(firstEl[0]) > 1:
            el = firstEl[0].pop()
            firstEl[1] -= el
            secoundEl[1] += el
            secoundEl[0].append(el) #to_sorted
            secoundEl[0].sort(reverse = True) 
            data[first], data[secound] = firstEl, secoundEl
        elif diff < x:
          if len(secoundEl[0]) > 1:
            el = secoundEl[0].pop()
            secoundEl[1] -= el
            firstEl[1] += el
            firstEl[0].append(el) #to_sorted
            firstEl[0].sort(reverse = True)
            data[first], data[secound] = firstEl, secoundEl
        self.processorsData = data
        #needs best tracking and saving in self.bestData
      n -= 1
      if max([x[-1] for x in data]) <= max([x[-1] for x in self.bestData]):
        self.bestData = deepcopy(data)
    print data
    print self.bestData
      
x = Normalizer([[28, 5, 3], [21, 6, 2], [20, 7, 1], [10, 7]],4)

x.swap(0, 10000)

#deepcopying need fix