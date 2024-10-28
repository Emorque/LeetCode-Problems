from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreq(w: str):
            freq = [0] * 26
            for char in w:
                freq[ord("a") - ord(char)] += 1
            return tuple(freq)

        anagrams = defaultdict(list)
        
        for word in strs:
            freq = getFreq(word)
            anagrams[freq].append(word)
        return list(anagrams.values())