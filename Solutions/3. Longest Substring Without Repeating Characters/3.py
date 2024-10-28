class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0

        seen = set()

        while right < len(s):
            char = s[right]

            if char in seen:
                longest = max(longest, right - left)
                while char in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(char)
            right += 1
        
        return max(longest, right - left)