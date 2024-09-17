#DFS WITH CACHING: 
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        hashmap = {}

        def dfs(s1Index, s2Index, s3Index):
            if s3Index >= len(s3):
                if s2Index >= len(s2) and s1Index >= len(s1):
                    return True
                return False
            elif s2Index >= len(s2):
                return s1[s1Index:] == s3[s3Index:]
            elif s1Index >= len(s1):
                return s2[s2Index:] == s3[s3Index:]
            
            if (s1Index, s2Index, s3Index) in hashmap:
                return hashmap[(s1Index, s2Index, s3Index)]

            if s1[s1Index] == s3[s3Index] and s2[s2Index] == s3[s3Index]:
                hashmap[(s1Index, s2Index, s3Index)] = dfs(s1Index + 1, s2Index, s3Index + 1) or dfs(s1Index, s2Index + 1, s3Index + 1)
            elif s1[s1Index] == s3[s3Index]:
                hashmap[(s1Index, s2Index, s3Index)] = dfs(s1Index + 1, s2Index, s3Index + 1)
            elif s2[s2Index] == s3[s3Index]:
                hashmap[(s1Index, s2Index, s3Index)] = dfs(s1Index, s2Index + 1, s3Index + 1)
            else:
                hashmap[(s1Index, s2Index, s3Index)] = False
            return hashmap[(s1Index, s2Index, s3Index)]
            
        return dfs(0,0,0)
    
# Solution without s3Index:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        hashmap = {}

        def dfs(s1Index, s2Index): 
            if s1Index + s2Index >= len(s3):
                if s2Index >= len(s2) and s1Index >= len(s1):
                    return True
                return False
            elif s2Index >= len(s2):
                return s1[s1Index:] == s3[s1Index + s2Index:]
            elif s1Index >= len(s1):
                return s2[s2Index:] == s3[s1Index + s2Index:]
            
            if (s1Index, s2Index) in hashmap:
                return hashmap[(s1Index, s2Index)]

            if s1[s1Index] == s3[s1Index + s2Index] and s2[s2Index] == s3[s1Index + s2Index]:
                hashmap[(s1Index, s2Index)] = dfs(s1Index + 1, s2Index) or dfs(s1Index, s2Index + 1)
            elif s1[s1Index] == s3[s1Index + s2Index]:
                hashmap[(s1Index, s2Index)] = dfs(s1Index + 1, s2Index)
            elif s2[s2Index] == s3[s1Index + s2Index]:
                hashmap[(s1Index, s2Index)] = dfs(s1Index, s2Index + 1)
            else:
                hashmap[(s1Index, s2Index)] = False
            return hashmap[(s1Index, s2Index)]

        return dfs(0,0)
    

#OPTIMIZED DP:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                # every cell is already False so if neither if statements execute, cell can be left alone
        return dp[0][0]