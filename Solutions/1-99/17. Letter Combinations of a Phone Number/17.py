from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combinations = []

        def helper(index, currentString):
            if index == len(digits):
                combinations.append(currentString[:])
                return
            
            for char in numpad[digits[index]]:
                helper(index + 1, currentString + char)

        helper(0, "")
        return combinations if digits else []