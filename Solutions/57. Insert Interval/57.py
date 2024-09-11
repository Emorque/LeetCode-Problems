from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            currInterval = intervals[i]

            if newInterval[0] > currInterval[1]:
                output.append(currInterval)
            elif newInterval[1] < currInterval[0]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], currInterval[0])
                newInterval[1] = max(newInterval[1], currInterval[1])

        output.append(newInterval)
        
        return output