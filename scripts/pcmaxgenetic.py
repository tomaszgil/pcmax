from pcmaxgreedy import PCMaxGreedy
from pcmaxrotate import PCMaxRotate

class PCMaxGenetic:
    def __init__(selfself, execTimes, procNum):
        self.execTimes = execTimes
        self.procNum = procNum

    def solve(self):
        # find the best greedy solution
        # swap tasks between longest with shortest (for a required number of repetions or until there's no change in outcome)
        # swap tasks between more than 2 processors
        # alongside swaps introduce mutations between longest and random

    def __del__(self):
        pass
