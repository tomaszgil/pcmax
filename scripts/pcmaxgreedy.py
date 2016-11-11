class PCMaxGreedy:
    def __init__(self, execTimes, procNum):
        self.execTimes = execTimes
        self.procNum = procNum

    def solve(self):
        sortedExecTimes = sorted(self.execTimes, reverse=True)
        processorsTime = [0] * 4

        for execTime in sortedExecTimes:
            earliestAvailableProcessor = processorsTime.index(min(processorsTime))
            processorsTime[earliestAvailableProcessor] += execTime

        return max(processorsTime)

x = PCMaxGreedy([6,7,8,10,4,3,2],4)
cmax = x.solve()
print(cmax)
