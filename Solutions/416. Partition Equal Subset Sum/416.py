from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False
        
        target = total // 2
        sums = set()
        sums.add(0) #ensures the current num gets added to sums

        for num in nums:
            if num == target:
                return True
            newSums = set()
            for currSum in sums:
                newSum = currSum + num
                newSums.add(currSum)
                if newSum == target:
                    return True
                if newSum > target:
                    continue
                newSums.add(newSum)
                
            sums = newSums

        return False