import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right= []

    def addNum(self, num: int) -> None:
        if self.right and self.right[0] < num:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, num * -1)

        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, heapq.heappop(self.left) * -1)
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, heapq.heappop(self.right) * -1)        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (self.right[0] + (self.left[0] * -1)) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()