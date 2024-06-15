1. Share 2 questions you would ask to help understand the question:
- What should be returned if the list is empty?
- Does the list have even or odd number of elements effect our algorithim?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Pointers (Likely)
- Sliding windows (Unlikely)
  
3. Write out in plain English what you want to do:
- We want to take two pointers and set them to the ends of the list
- While those pointers have yet to cross each other
  - Calculate the midpoint and compare it to our target
    - If there is a match, return the index
    - If not, then adjust the pointers and repeat the cycle until the target is found
- If pointer have crossed each other, return -1

4. Translate each sub-problem into pseudocode:
- What we want to do is traditional binary search, which can be performed becuase it list is already sorted for us
- To do Binary Search, we first take two pointers, one at each end of the list
- Then we calculate the midpoint between those two pointers, and set it our mid
- Then, we the mid value to our target
  - If match, return the index
  - Else, we continue with the loop
    - If the target is greater than the mid, set the left pointer to the mid + 1
    - Else if the target is less than the mid, set the right pointer to the mid - 1
    - Now, calculate the midpoint again and repeat the process 
  - Do this until the left and right pointers pass each other
- If they do, there is no target in our list, so we return -1 


5. Translate the pseudocode into Python and share your final answer:
  <!-- 
  def search(nums: List[int], target: int) -> int:
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = low + ((high - low) // 2)
    if nums[mid] == target:
      return mid
    if nums[mid] > target:
      high = mid - 1
    else:
      low = mid + 1
  return -1
  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it does the the algorithm in O(logn) time
- One weak area is that mid could have been calcualuted more effectively. 