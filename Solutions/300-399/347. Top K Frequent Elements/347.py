from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freqList = [[] for i in range(len(nums) + 1)]
        for key, value in freq.items():
            freqList[value].append(key)

        kthList = []
        for i in range(len(freqList) - 1, -1, -1):
            if freqList[i] == []:
                continue
            for num in freqList[i]:
                kthList.append(num)
                if len(kthList) == k:
                    return kthList
        return kthList