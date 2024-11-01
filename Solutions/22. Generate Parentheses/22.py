from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def backtrack(combination, opening, closing):
            if closing == n:
                combinations.append(combination)
                return
            if opening < n:
                backtrack(combination + "(", opening + 1, closing)
            if closing < opening:
                backtrack(combination + ")", opening, closing + 1)
        backtrack("(", 1, 0)
        return combinations