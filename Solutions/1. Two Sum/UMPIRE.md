1. Share questions you would ask to help understand the question:
- Can there be duplicate numbers? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash map (Likely)
- Two pointers (Likely)

3. Write out in plain English what you want to do:
- A hash map can be created to solve this problem, with the key being the value at a certain index, and then the value being the index 
- This hashmap will be filled as the nums list is travered:
    - and, through calculations, if the target is found, return the key index and current index 

4. Translate each sub-problem into pseudocode:
- Initialize a map 
- Iterate through the nums list:
    - if the num is not in the map, then added it to the map (target-num) with the value as the current index
    - if it is, then return [key, current index]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[target-num] = i
            else:
                return [i, hashmap[num]]
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this is done in O(n) time, and the algorithm ends once the two sum is found
- One weak area is that it could be more readable 