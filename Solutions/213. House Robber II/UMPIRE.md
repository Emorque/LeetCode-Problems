1. Share questions you would ask to help understand the question:
- Is there at least one house?
- Can houses have negative money?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- After going through some examples, I realized that without using some helper function or maybe another data strucutre, it is tough to know that the path I as a robber has taken, has been one where I robbed the first house. The reason this is important, is because I do need to know this to check if I am able to rob the last house
- Then, I realized, what if I just pretended these hosues where in a straight block, expect the is a block of the first house to the second to last house, and then a block of the second house to the last house
- Then, I can just get the max bounty of each block, and then return the max between them
- I can do this dynamically and I don't think reuisng the same array twice changes the outcome?
- But just in case, I'll use other int variables


4. Translate each sub-problem into pseudocode:
- Intiailzie two bounty ints to 0

- for i in range(0, len(nums) - 1):
  - temp = max(nums[i] + b1, b2)
  - b1 = b2
  - b2 = temp

- bounty = b2
- b1, b2 = 0,0

for i in range(1, len(nums)):
  - temp = max(nums[i] + b1, b2)
  - b1 = b2
  - b2 = temp

return max(bounty, b2)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        b1, b2 = 0, 0

        for i in range(len(nums) - 1):
            temp = max(nums[i] + b1, b2)
            b1 = b2
            b2 = temp

        bounty = b2

        b1, b2 = 0, 0

        for i in range(1, len(nums)):
            temp = max(nums[i] + b1, b2)
            b1 = b2
            b2 = temp

        return max(bounty, b2) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution is done by only traversing the nums array twice, with no extra data structures, so the time in O(n) and the space is O(1)
- One weak area is that since I am using the same for loop twice, I could have simplified the code by the creating a helper function with the same logic and just calling it twice with different starting, ending indexes