from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    temp = stack.pop()
                    temperatures[temp] = i - temp 
                stack.append(i)
        while stack:
            temperatures[stack.pop()] = 0
        return temperatures