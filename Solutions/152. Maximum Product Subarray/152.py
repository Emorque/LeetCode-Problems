from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = []
        maxProduct = nums[0]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(products)):
                product = nums[i] * products.pop(0)
                maxProduct = max(maxProduct, product)
                if product not in products or nums[i] == -1:
                    products.append(product)
            products.append(nums[i])
            maxProduct = max(maxProduct, nums[i])
        
        return maxProduct
    


# more time efficient solution
# https://www.youtube.com/watch?v=lXVy6YWFcRM&t=10s
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums) #something like 0 isn't a good default case because we can have something like [-1]
        currMin, currMax = 1, 1 # 1 is a good neutral value

        for n in nums:
            if n == 0: # we don't want to mess up our current min and max, so reset the currMin and currMax. Now, everything before this 0 cannot be considered for subarrays to the left of the 0
                currMin, currMax = 1, 1
                continue
            temp = currMax * n
            currMax = max(n * currMax, n * currMin, n) # [-1, 8] we do want to check the current index
            currMin = min(temp, n * currMin, n) # [-1, -8] we still want -1 

            output = max(output, currMax)
        return output