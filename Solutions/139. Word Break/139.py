from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        match = [False] * (len(s) + 1)
        match[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(s) - i >= len(word) and s[i:len(word) + i] == word:
                    match[i] = match[i + len(word)]
                if match[i]:
                    break
        return match[0]