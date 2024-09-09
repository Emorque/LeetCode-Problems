1. Share questions you would ask to help understand the question:
- Are duplicate numbers in the candidates list considered as a duplicate in a viable combination
    - ex: 1 appears twice, so can a combination be [1,1, ...]?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Backtracking (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- Having drawn a decision tree, I got stuck on how to handle duplicate combinations.
- However, after trying with the candidates list already sorted, I think I have an idea
- Create a dfs helper function
- Both in this function and the outer function that calls dfs, have a set, and append numbers that get added to a current list also to a set
- if a following number is in that set, don't perform dfs on it.

4. Translate each sub-problem into pseudocode:
- Initialize an output and currList list, and a startSet
- get the length of candidates

- create a dfs function(currentSum, currentIndex):
    <!-- - if currentSum == target:
        - output.append(currList.copy())
        - return
     -->
    - subset = set()

    - for i in range(currentIndex, candLength):
        - if candidates[currentIndex] in set:
            - continue
        - if currentSum + candidates[currentIndex] == target:
            - currList.append(candidates[currentIndex])
            - output.append(currList.copy())
            - currList.pop()
        - elif currentSum + candidates[currentIndex] < target:
            - currList.append(candidates[currentIndex])
            - dfs(currentSum + candidates[currentIndex], i)
        - else:
            break
    
- for c in range(candLength):
    - if candidates[c] == target:
        - output.append([target])
        - break
    - elif candidates[c] > target:
        - break
    - if candidate[c] in set:
        - continue
    - currList.append(candidate[c])
    - dfs(candidate[c], c + 1)
    - currList.pop()
    - startSet.add(candidate[c])

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output, currList = [], []
        candidates.sort()
        startSet = set()
        candLength = len(candidates)

        def dfs(currSum, currIndex):
            subset = set()

            for i in range(currIndex, candLength):
                currCand = candidates[i]
                if currCand in subset:
                    continue
                subset.add(currCand)
                if currSum + currCand == target:
                    currList.append(currCand)
                    output.append(currList.copy())
                    currList.pop()
                elif currSum + currCand < target:
                    currList.append(currCand)
                    dfs(currSum + currCand, i + 1)
                    currList.pop()
                else:
                    break
        for c in range(candLength):
            currCand = candidates[c]
            if currCand == target:
                output.append([target])
                break
            elif currCand > target:
                break
            if currCand in startSet:
                continue
            currList.append(currCand)
            dfs(currCand, c + 1)
            currList.pop()
            startSet.add(currCand)
        
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the utility of sets and backtracking/dfs is used so that any and all potentially duplicate subsets and unviable combinations are never processed
- One weak area is that to achieve, there are a lot of checks, so some comments explaining why mutliple breaks and continues are used can help make reasoning more clear