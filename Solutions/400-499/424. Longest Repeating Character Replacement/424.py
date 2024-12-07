class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left, right = 0,0
        freq = {}

        maxFreq = 0

        while right < len(s):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            if freq[s[right]] > maxFreq:
                maxFreq = freq[s[right]]
            if (right - left + 1) > maxFreq + k:
                # no longer valid
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return max(right - left, longest)