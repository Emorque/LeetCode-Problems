1. Share questions you would ask to help understand the question:
- Can target be 0 or a negative number?
- Is the array sorted?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Backtracking (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking of, is creating a dfs backtracking algorithm, that will hold onto a currList that gets every number on and after the intial num added onto it.
- If the sum of elements in the array is equal to target, a copy of that array will be appended to an output list

4. Translate each sub-problem into pseudocode:
- Initialize a list for output, currList
- Get the length of candidates

- Create a dfs helper function(currSum, currIndex):
  <!-- - if currSum > target:
    - return  -->
  - for i in range(currIndex, candidatesLength):
    - if currSum + candidiates[currIndex] == target:
      - currList.append(candidates[currIndex])
      - output.append(currList.copy())
      - return
    - elif currSum + candidates[currIndex] < target:
      - currList.append(candidates[currIndex])
      - dfs(currSum + candidates[currIndex], currIndex)
      <!-- - currIndex += 1 -->
      - currIndex.pop()
    
- for i in range(candidatesLength):
  - if candidates[i] == target:
    - output.append([target])
  - elif candidates[i] < target:
    - currList.append(candidates[i])
    - dfs(candidates[i], i)

- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, currList = [], []
        candLength = len(candidates)

        def dfs(currSum, currIndex):
            for i in range(currIndex, candLength):
                currNum = candidates[i]

                if currSum + currNum == target:
                    currList.append(currNum)
                    output.append(currList.copy())
                    currList.pop()
                elif currSum + currNum < target:
                    currList.append(currNum)
                    dfs(currSum + currNum, i)
                    currList.pop()
        
        for c in range(candLength):
            if candidates[c] == target:
                output.append([target])
            elif candidates[c] < target:
                currList.append(candidates[c])
                dfs(candidates[c], c)
                currList.pop()

        return output  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm uses backtracking and dfs to check every possible decision to made at a certain point when building a potential list
- One weak area is that there is a lot of popping and appending, so some comments can be it more readable to track what is happening