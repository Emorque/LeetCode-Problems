class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""

        def helper(left, right):
            nonlocal substring
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left > len(substring):
                substring = s[left + 1:right]

        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
            
        return substring