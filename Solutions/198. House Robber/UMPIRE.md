1. Share questions you would ask to help understand the question:
- Is there at least one house?
- Are there houses with negative money?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- After drawing some examples, I think using DP would be a great technique for saving the amount of potential earnings at each house
- First, let us consider examples:
  - If the number of houses is 1, return that house
  - If 2, return the house with the max
  - If 3, that third house always appreciates having the earnings of the 1 house, so add those two, and then return the max of the second and third house
  - If 4 and up, this is where its gets interesting 
    - Like with 3, we can add a previous house's cost to our current house, so long as it isn't directly next to it. So, with house 4 for example, we can get the max of houses 1 and 2, not considering three. 
    - The reason two hosues are checked and not more is that, after two, there is deminishing returns. 
      - Even with an example with [0,0,4,0,0,0,6], using that logic, it would become [0,0,4,0,4,4,10]. If we considered three houses, then the same result would happen. 
    - Basically, from index 3 onward, we want to add the max of houses[i - 2] and houses[i - 3] to our current cost
- Then at the end, return the max of the last two houses, since maybe the second to last house has greater earnings, and when finding the earnings of the last house, that second to last isn't considered, so it should be considered here

4. Translate each sub-problem into pseudocode:
- If nums == 1:
  - return nums[0]

- if nums >= 3:
  - nums[2] += nums[1]

- for i in range(3, len(nums)):
  - nums[i] += max(nums[i - 2], nums[i  - 3])

- return max(nums[-1], nums[-2])

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def rob(self, nums: List[int]) -> int:
        numsLength = len(nums)

        if numsLength == 1:
            return nums[0]
        
        if numsLength >= 3: 
            nums[2] += nums[0]
        
        for i in range(3, numsLength):
            nums[i] += max(nums[i - 2], nums[i - 3])
        
        return max(nums[-1], nums[-2]) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that DP is used to always have in memory, the highest amount of earnings for that houses in nums
- One weak area is that I did uses 2 if statements to not mess up my for loop, which makes it more complicated that other solutions