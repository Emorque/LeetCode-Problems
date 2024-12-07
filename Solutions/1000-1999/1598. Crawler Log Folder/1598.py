from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0

        for log in logs:
            if (log[0] != '.'):
                level += 1
            elif (log == "../"): 
                if level > 0:
                    level -= 1
        return level