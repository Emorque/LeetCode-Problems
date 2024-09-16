class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        left, right = 0,0
        leftI, rightI = 0, 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if (right - left - 1) > maxLength:
                maxLength = right - left - 1
                leftI = left + 1
                rightI = right - 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if (right - left - 1) > maxLength:
                maxLength = right - left - 1
                leftI = left + 1
                rightI = right - 1
            
        return s[leftI:rightI + 1]