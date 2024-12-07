from typing import List
import heapq

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            currStart, currEnd = interval.start, interval.end
            if not minHeap:
                heapq.heappush(minHeap, currEnd)
            elif minHeap[0] > currStart:
                heapq.heappush(minHeap, currEnd)
            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, currEnd)
        return len(minHeap)