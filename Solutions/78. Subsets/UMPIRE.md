1. Share questions you would ask to help understand the question:
- Can this be thought of like a tree?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)

3. Write out in plain English what you want to do: 
- After drawing out a decision tree, each level of the tree basically represents if the current number was added or not to the current list
- At every level, this means that the number of lists grows by 2x, which makes sense, since the number either gets added or not
- This can be done via a helper function that will travel down the path, carrying it's current subset, until it reaches the very end (the entire nums array has been traversed for this list)
- At this point, the resulting list gets appended to a general output list

4. Translate each sub-problem into pseudocode:
- initialize an output list
- numsLength = len(nums) 
- create a dfs helper function (currList, currIndex):
  - if currIndex == numsLength:
    - append currList to output
    - return 
  - dfs(currList, currIndex + 1)
  - currList.append(nums[currIndex])
  - dfs(currList, currIndex + 1)
- dfs([], 0)
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!--  class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, currList = [], []
        numsLength = len(nums)

        def dfs(currIndex):
            if currIndex == numsLength:
                output.append(currList.copy())
                return
            currList.append(nums[currIndex])
            dfs(currIndex + 1)
            currList.pop()
            dfs(currIndex + 1)

        dfs(0)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm is decently easy to follow, with each decision represented by the two dfs statements in the dfs function. Adding or not adding the current num 
- One weak area is that this was a rework, since I realized python was not appending a copy of the currList originally. Therefore, currList was removed as a parameter, and so, is adjusted for each dfs call. A copy is then appended to the output. Without this, it would still get edited afterwords. 