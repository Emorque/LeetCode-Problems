from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end) -> int:
            house1, house2 = 0, 0

            for i in range(start, end):
                cash = nums[i]

                temp = max(house1 + cash,house2)
                house1 = house2
                house2 = temp
            
            return house2

        if len(nums) == 1:
            return nums[0]
            
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))