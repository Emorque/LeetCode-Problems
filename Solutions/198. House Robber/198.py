from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])

        # nums[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        
        # return nums[-1]

        # Above works, bottom with remove that need of the first 5 lines of code

        house1, house2 = 0,0

        for num in nums:
            temp = max(num + house1, house2)
            house1 = house2
            house2 = temp
        
        return house2