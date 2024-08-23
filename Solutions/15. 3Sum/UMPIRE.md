1. Share questions you would ask to help understand the question:
- Can there be no solutions in a test case?
- Can the same number be used for multiple triplets?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely 
- Set (Likely)
- Hash map (Likely)

3. Write out in plain English what you want to do: 
- The end goal is to find a set of triplets that each equal to 0. There are some unique cases, where there can be no triplets, or that some numbers appear in multiple triplets
- What this has me thinking, is that to ensure that all triplets are found, each number has to be traversed
- Then for each pairing found, append it to the output set, and return that at the end

4. Translate each sub-problem into pseudocode:
- Initialize an output set 
- Create a loop that iterates through each numner in the nums list
  - In this traversal, each number is made into a target 
    - Then, traversal from the current number all the way to the right, and find all pairs that sum to the target 
    - Append any found pairs into the output set
    - Even if a pair is found, keep iterating, since one number can appear in multiple triplets
- Return the output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        visited = set()

        for i in range(len(nums) - 2): 
            if nums[i] in visited:
                continue
            target = nums[i] * -1
            hashmap = {}
            for j in range(i + 1, len(nums)):
                if nums[j] not in hashmap:
                    hashmap[target-nums[j]] = nums[j]
                else:
                    curr = (nums[i], hashmap[nums[j]], nums[j])
                    curr = tuple(sorted(curr))
                    triplets.add(curr)
            visited.add(nums[i])
        return triplets -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area of the algorithm is that it uses a visited set, so that whenever a number has been a target, and all the numbers to the right have been traversed, there is no need to traverse with that number as a target again, so it gets skipped
- One weak area is that it can be a bit confusing what is going on, compared to other solutions that start with a sorted list 
- And I am not a fan of how I used sorted here, since I had trouble figuring out how to use the triplets set on tuples, since (1,2,3) and (3,2,1) are not considered distinct