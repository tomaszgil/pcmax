class PCMaxGreedy:
    def __init__(self, execTimes, procNum):
        self.execTimes = execTimes
        self.procNum = procNum

    def solve(self):
        sortedExecTimes = sorted(self.execTimes, reverse=True)
        processorsData = [[] for i in range(self.procNum)]

        for execTime in sortedExecTimes:
            processorsTime = [sum(processor) for processor in processorsData]
            earliestAvailableProcessor = processorsTime.index(min(processorsTime))
            processorsData[earliestAvailableProcessor].append(execTime)

        cmax = max([sum(processor) for processor in processorsData])
        return processorsData, cmax

x = PCMaxGreedy([6,7,8,10,4,3,2],4)
order, cmax = x.solve()
print(order, cmax)
