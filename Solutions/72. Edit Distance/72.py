class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # cache = {}
        dp = [[float("inf")] * (len(word1) + 1) for i in range(len(word2) + 1)] 
        dp[-1][-1] = 0

        for j in range(len(word1) + 1):
            dp[len(word2)][j] = len(word1) - j
        for i in range(len(word2) + 1):
            dp[i][len(word1)] = len(word2) - i

        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

        # def helper(index1, index2):
        #     if (index1, index2) in cache:
        #         return cache[(index1, index2)]
        #     if index2 == len(word2) and index1 == len(word1):
        #         return 0
        #     if index2 == len(word2):
        #         return len(word1) - index1
        #     if index1 == len(word1):
        #         return len(word2) - index2
            
        #     if word1[index1] == word2[index2]:
        #         return helper(index1 + 1, index2 + 1)
        #     cache[(index1, index2)] = 1 + min(helper(index1, index2 + 1), helper(index1 + 1, index2), helper(index1 + 1, index2 + 1))
        #     return cache[(index1, index2)]
            
        return dp[0][0]