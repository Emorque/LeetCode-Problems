from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        hashSet = set(hashMap.values())
        return len(hashMap.values()) == len(hashSet)