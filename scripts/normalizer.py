from random import randint

class Normalizer:
  def __init__(self, processorsData, procNum):
    self.procNum = procNum
    self.processorsData = [[singleData,sum(singleData)] for singleData in processorsData]

  def swap(self, x):
    data = self.processorsData
    print data
    first, secound = randint(0, len(data)-1), randint(0, len(data)-1)
    if first != secound:
      firstEl, secoundEl = data[first], data[secound]
      diff = firstEl[1] - secoundEl[1]
      print firstEl[1], secoundEl[1], diff
      if diff > x:
        if len(firstEl[0]) > 1:
          el = firstEl[0].pop()
          secoundEl[0].append(el) #to_sorted
          firstEl[1] -= el
          secoundEl[1] += el
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
      #instance grade > the best:
      self.processorsData = data
      
x = Normalizer([[28, 5, 3], [21, 6, 2], [20, 7, 1], [10, 7]],4)

[30, 15, 10] - > [30, 16]
[30, 15] , [30, 16, 10]

i = 1
while(i):
  x.swap(1)
  i -= 1