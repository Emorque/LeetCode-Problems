from typing import List

class DetectSquares:

    def __init__(self):
        self.frequency = {}
        self.points = []

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.frequency:
            self.points.append(point)
            self.frequency[(point[0], point[1])] = 0
        self.frequency[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        output = 0
        x, y = point
        for xi, yi in self.points: 
            if abs(x - xi) == abs(y - yi) and (x != xi and y != yi):
                if (x, yi) in self.frequency and (xi, y) in self.frequency:
                    output += 1 * self.frequency[(xi, yi)] * self.frequency[(x, yi)] * self.frequency[(xi, y)]
        return output

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)