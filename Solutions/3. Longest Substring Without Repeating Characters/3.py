class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        output = 0
    
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            else:
                while s[left] != s[i]:
                    del hashmap[s[left]]
                    left += 1
                left += 1
            output = max(output, i - left + 1)
        return output