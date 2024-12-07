from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key=lambda x: x[0])

        currInterval = intervals[0]

        for i in range(1, len(intervals)):
            if currInterval[1] >= intervals[i][0]:
                currInterval[1] = max(currInterval[1], intervals[i][1])
            else:
                output.append(currInterval)
                currInterval = intervals[i]
        output.append(currInterval)
        return output