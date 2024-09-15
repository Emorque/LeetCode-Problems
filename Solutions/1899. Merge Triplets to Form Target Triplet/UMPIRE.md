1. Share questions you would ask to help understand the question:
- Can an element in the target not exist in the triplets array?
- Can any element be negative?
- How many triplets can there be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Iterating?

3. Write out in plain English what you want to do: 
- After messing with some targets, there are a few things that I realized
- 1. If a triplet has even one element that is greater than an element in target, it cannot be considered for a merge, since even if 2 elements are equal to target, merging with this would never give us target 
- 2. If the triplets array is traversed, and not all of the elements in target were found, then no amount of merges can give us target
- Using these rules, I thought of how triplets can be iterated once 
- Have three seperate booleans for each element in target:
  - if all of the elements in the current triplet are less than or equal to the respective elements in target, 
    - then check if any are equal
      - if they are, set that elements corresponding boolean to true
  - if all of the booleans are true, then return True
- if the triplets array was traversed, and not all of the booleans are true, then return False as no set of merged triplets in the list can result in target

4. Translate each sub-problem into pseudocode:
- Initailize 3 booleans for each element in target
- Iterate through the triplets list
  - if all of the booleans are True, return True, no need to iterate further
  - if any of the elements in the current triplet is greater than the corresponding element in t, ignore it, even if its only one element and the other two match completely, it can never be considered for a merge
  - if any of the elements in the current triplet are equal, set the corresponding boolean to True
- if the end is reached, return boolean 1, boolean 2, and boolean 3 (maybe the last one triplet turns the test case to True, so the check in the loop was skipped) (in that case, return True)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target1 = target[0]
        target2 = target[1]
        target3 = target[2]

        t1Found = False
        t2Found = False
        t3Found = False

        for i, j, k in triplets:
            if t1Found and t2Found and t3Found:
                return True
            if i > target1 or j > target2 or k > target3:
                continue
            if i == target1:
                t1Found = True
            if j == target2:
                t2Found = True
            if k == target3:
                t3Found = True
        
        return t1Found and t2Found and t3Found  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a set of booleans are used to check if, at anypoint, a set of triplets can build the target. And since we only can about wether if the target can be built, there is no need to build another build data structure
- One weak area is that there are a lot of variable names to make readible good, but it can be pain point as the first 3 variables are not neccessary