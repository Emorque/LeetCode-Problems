from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        p1 = 0
        stack = []
        spilled = False

        while p1 != len(height)-1:
            if height[p1] == 0:
                p1 += 1 
                continue
            p2 = p1 + 1
            while height[p2] < height[p1]:
                if p2 == len(height) - 1:
                    stack.append(height[p2])
                    spilled = True
                    break
                stack.append(height[p2])
                p2 += 1
            if spilled: 
                right = stack.pop()
                while stack:
                    temp = stack.pop()
                    if right > temp:
                        output += right - temp
                    else:
                        right = temp
                return output
            while stack:
                output += height[p1] - stack.pop()
            p1 = p2
        return output