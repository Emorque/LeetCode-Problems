1. Share questions you would ask to help understand the question:
- Can the nums list be empty?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Backtracking (Likely)
- DFS (Likely)
- Set (Likely)

3. Write out in plain English what you want to do: 
- Thanks to drawing out a decision tree, I think using a backtracking algorithm with dfs would work
- Since I want to adjust the nums list, I think duplicating it to be a set would be better, as removing is O(1)
- Create a dfs helper function:
    - that checks if any numbers are in a seen set. If the number isnt appends it to the currList. 
    - then, call dfs and then remove that number from the seen set
- create a while loop that iterates through the nums list with a similar logic

4. Translate each sub-problem into pseudocode:
- initialize a seen set
- intiailize an output, currList list 
- get the length of the nums list
- create a dfs helper function(currLength)
    - if currLength == numsLength:
        - append a copy of currList to output
        - return
    - for i in range(numsLength):
        - if nums[i] not in set:
            - currList.append(nums[i])
            - set.add(nums[i])
            - dfs(currLength + 1)
            - currList.pop()
            - set.remove(nums[i])
- for num in nums:
    - set.add(num)
    - currList.append(num)
    - dfs(1)
    - set.remove(num)
    - currList.pop()

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        output, currList = [], []

        numsLength = len(nums)

        def dfs(currLength):
            if currLength == numsLength:
                output.append(currList.copy())
                return
            for i in range(numsLength):
                if nums[i] not in seen:
                    currList.append(nums[i])
                    seen.add(nums[i])
                    dfs(currLength + 1)

                    currList.pop()
                    seen.remove(nums[i])

        for num in nums:
            seen.add(num)
            currList.append(num)
            dfs(1)
            seen.remove(num)
            currList.pop()

        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that backtracking is used to continually build a list to be appended to the output
- One weak area is that for loop in the dfs function. I was having trouble thinking how I can check the list for "seen" numbers
    - I thought of trying to pass a subList as a parameter, sort of like a part of the nums list gets sent without the appended num
        - I couldn't wrap my head on an implementation of it, so I landed on this more brute force check 