class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        freq = {}

        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        
        left = 0
        constructing = False
        for right, char in enumerate(s2):
            if constructing:
                if char in freq and freq[char] == 1 and (right - left + 1) == s1_len:
                    return True
                if char not in freq:
                    while left < right:
                        freq[s2[left]] += 1
                        left += 1
                    constructing = False
                elif freq[char] == 0:
                    while s2[left] != char:
                        freq[s2[left]] += 1
                        left += 1
                    left += 1
                else:
                    freq[char] -= 1
            elif char in freq:
                    freq[char] -= 1
                    constructing = True
                    left = right
                    if (right - left + 1) == s1_len:
                        return True
        return False