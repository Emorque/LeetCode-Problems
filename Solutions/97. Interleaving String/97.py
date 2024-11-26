# decision tree with caching
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #s3Index = s1Index + s2Index
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {} #(s1Index, s2Index) : bool

        def helper(s1Index, s2Index):
            if (s1Index, s2Index) in cache:
                return cache[(s1Index, s2Index)]
            if s1Index + s2Index == len(s3):
                return True
            if s1Index + s2Index > len(s3):
                return False
            
            res = False
            if s1Index < len(s1) and s1[s1Index] == s3[s1Index + s2Index]:
                res = helper(s1Index + 1, s2Index)
            if s2Index < len(s2) and s2[s2Index] == s3[s1Index + s2Index]:
                res = res or helper(s1Index, s2Index + 1)
            cache[(s1Index, s2Index)] = res
            return res
        
        return helper(0, 0)
    
# dp non optimized solution
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
