from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def helper(open: int, close: int, currStr: str):
            if open == n and close == n:
                output.append(currStr)
                return
            if open == n:
                helper(open, close + 1, currStr+')')
            elif open <= close:
                helper(open + 1, close, currStr+'(')
            else:
                helper(open + 1, close, currStr + '(')
                helper(open, close + 1, currStr + ')')
        helper(0, 0, "")
        return output