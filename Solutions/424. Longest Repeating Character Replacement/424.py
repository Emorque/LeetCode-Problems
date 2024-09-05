class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        output = 0

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
            if (i - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            output = max(output, i - left + 1)
        return output

