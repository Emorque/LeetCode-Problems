from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasSum = 0
        tank = 0
        station = 0

        for i in range(len(gas)):
            gasGain = gas[i] - cost[i]
            tank += gasGain
            if tank < 0:
                station = i + 1
                tank = 0
            gasSum += gasGain
        
        return station if gasSum >= 0 else -1