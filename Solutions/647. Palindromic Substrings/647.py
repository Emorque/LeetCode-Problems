class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        def helper(left, right):
            nonlocal palindromes
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
                palindromes += 1

        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        return palindromes