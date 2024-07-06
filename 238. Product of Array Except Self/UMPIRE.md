1. Share 2 questions you would ask to help understand the question:
- Is it okay to use extra space?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Multiple Passes (Likely)
- 2 pointers (Likely)

3. Write out in plain English what you want to do: 
- There is a restriction to take note of: "without using the division operation"
- Multiple passes can be used, to grab the prefix and suffix products
- This has to be done because the product in the index of the answer array cannot include the corresponding val in the index of nums
- Start off with an answer array
- Iterate through the list from left to right to calculate, calculating and remembering the prefix product and adding it to the answer array
- Do the same from right to left, calculating the suffix product
- return the answer array 

4. Translate each sub-problem into pseudocode:
- initialize the answer array with the same size as the nums array
- initialize the prefix and suffix products as 1
- create a for loop that goes from left to right in the nums array.
  - multiply the current index in answer by the prefix product
  - multiple the prefix product by the current val in nums
- create a for loop that goes from right to left in the nums array.
  - multiply the current index in answer by the suffix product
  - multiple the suffix product by the current val in nums
- return the answer array

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        answer = [1] * len(nums)

        for i, num in enumerate(nums):
            answer[i] *= prefix
            prefix *= num

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm runs with O(1) space complexity since we just iterate through nums without more than needed data structures
- One weak area is that we are using a data structure. Another solution that I thought off that takes less space but more time, is to do an in-place algorithm.
  - What if we iterate through the nums, from left to right.
  - have a prefix product variable like the above solution set to 1
  - For every iteration
    - Set a pointer and caculate the suffix product.
    - Set the current index to prefix multiplied by suffix and multiply prefix by the current value before. A temp could be used here
  - The issue is that we essentially calculate the suffix product each time, but it is a solution that does work in-place.  