1. Share questions you would ask to help understand the question:


2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Can the nums List be empty?

3. Write out in plain English what you want to do:
- This problem can be solved through the use of a set. Sets inheritally cannot hold duplicates
- So, all I have to do is traverse through the nums list, populating a set with numbers. 
- Then, once a duplicate number is found, return true
- If I have traversed through the whole nums with no duplicates, return false

4. Translate each sub-problem into pseudocode:
- initiaize a set
- iterate through the nums
    - if the num is in set, return true
    - else, add the num to the set
- return false

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            if num in numsSet: return True
            else: numsSet.add(num)
        return False -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that only one traversal is needed and the algorithm ends as soon as the duplicate is found
- One weak area is that it could be made more readable