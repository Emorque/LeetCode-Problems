class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for char in s:
            if char == '*':
                leftMin -= 1
                leftMax += 1
            elif char == '(':
                leftMin += 1
                leftMax += 1
            else:
                leftMin -= 1
                leftMax -= 1
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        return leftMin == 0 