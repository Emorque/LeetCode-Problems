from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = []
        digitsLen = len(digits)

        if digitsLen == 0:
            return output

        def dfs(currIndex, currString):
            if currIndex == digitsLen:
                output.append(currString)
                return
            for c in numpad[digits[currIndex]]:
                dfs(currIndex + 1, currString + c)
        dfs(0, "")
        return output