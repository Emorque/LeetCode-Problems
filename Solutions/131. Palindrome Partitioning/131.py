from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output, currList = [], []
        sLen = len(s)

        def isPalindrome(subString):
            p1, p2 = 0, len(subString) - 1

            while p1 < p2:
                if subString[p1] != subString[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True

        def dfs(subString):
            if len(subString) == 0: 
                output.append(currList.copy())
                return
            for i in range(len(subString)):
                if isPalindrome(subString[:i + 1]):
                    currList.append(subString[:i + 1])
                    dfs(subString[i + 1:])
                    currList.pop()
        dfs(s)
        return output