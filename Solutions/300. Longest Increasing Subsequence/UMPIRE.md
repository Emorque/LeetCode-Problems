1. Share questions you would ask to help understand the question:
- Will nums have at least one integer?
- Can there negative ints?
- What is the range of the number of elements that can be expected?
- If a consecutive number is equal, is the subsequence no longer considered increasing?
- Do the values have to be consecutive?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- Drawing out the subsequence as a decision tree can get lengthy, but I realized that for some parts of a subsequence, they are repeateed. For example, I had the test case: [1,2,3,4,3]
  - The subsequence [3,4] would repeat multiple times, so if I could somehow document the current length of the longest subsequence at index 2, I wouldn't have to keep going all the end to the end each time
- That led me to think about instead going from right to left
  - Here, I would track the longest increasing subsequence in some cache list
    - Then as I progress to the left, I would set the value of the current index in the cache to the max(current length (which should be 1 for all since each index can be its own subsequence), and cache[i + x]... if the value is greater than it)
- This way, I don't have to recalculate the longest subsequence each time, once I have it for an index, I can just get that int value each time 

4. Translate each sub-problem into pseudocode:
- Initialize a cache of len(nums) where each value starts at 1

- start a for loop that goes from right to left:
  - for another loop that iterates from the current index to the right:
    - if the num is greater than the current num (increasing): 
      - set cache[index] = max(cache[index], 1 + cache[num])

- return the max int in cache

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 + cache[j])
        
        return max(cache) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a cache is used to quickly store and reference from the longest subsequence at each index
- One weak area is that this solution is clear with the diagram I drew, so without it can the explaination, why this solution works may not be clear