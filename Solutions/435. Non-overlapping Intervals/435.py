from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        output = 0  
        currInterval = intervals[0]

        for i in range(1, len(intervals)):
            if currInterval[1] > intervals[i][0]:
                output += 1
                currInterval[1] = min(currInterval[1], intervals[i][1])
            else:
                currInterval = intervals[i]
        return output