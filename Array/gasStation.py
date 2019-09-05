class Solution:
    def canCompleteCircuit(self, gas, cost):
        start, total, final =0, 0, 0
        for i in range(len(gas)):
            final += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        if final >= 0:
            return start
        else:
            return -1