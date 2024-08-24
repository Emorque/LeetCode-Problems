from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        road = []
        stack = []
        for i, num in enumerate(position):
            road.append([num, speed[i]])
        
        road = sorted(road)

        for j in range (len(road) - 1, -1, -1):
            tt = (target - road[j][0]) / road[j][1]
            if not stack: 
                stack.append(tt)
            elif stack and stack[-1] < tt:
                stack.append(tt)
        return len(stack)