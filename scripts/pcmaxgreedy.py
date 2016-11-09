class PCMaxGreedy:
    def __init__(self, instance):
        self.processorsNumber = instance.processorsNumber
        self.processesTimes = instance.executionTimes
        self.findCMax()
        
    def findCMax(self):
        sortedProcessesTimes = sorted(self.processesTimes)
        processorsTime = [0] * 4
        for processTime in sortedProcessesTimes:
            earliestAvailableProcessor = processorsTime.index(min(processorsTime))
            processorsTime[earliestAvailableProcessor] += processTime
        self.CMax = max(processorsTime)
        
class Instance:
    pass

instance = Instance()
instance.processorsNumber = 4 
instance.executionTimes = [5,3,6,1,2,4,2,2,5,6,2]
pcmax = PCMaxGreedy(instance)
print(pcmax.CMax)
