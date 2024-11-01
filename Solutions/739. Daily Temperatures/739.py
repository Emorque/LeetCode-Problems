from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        indexes = []

        for i, temp in enumerate(temperatures):
            while indexes and temperatures[indexes[-1]] < temp:
                prev_day = indexes.pop()
                answer[prev_day] = i - prev_day
            indexes.append(i)
        return answer 