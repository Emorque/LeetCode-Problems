1. Share questions you would ask to help understand the question:
- Are the values ascending by a value of 1 before any rotations? ex: [1,2,3,4,5,6,7]
- Can there be any negative values?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Binary Search (Likely)
- Two Pointer (Likely)

3. Write out in plain English what you want to do: 
- Given the natural of the question, it has me thinking of trying a modified version of binary search 
- Since the number of rotations are not given, there has to be some checks 
- If mid is greater than the right, then for sure everything between left and mid cannot be mid 
- if that isn't true, then high can be set to mid 

4. Translate each sub-problem into pseudocode:
- set low, high to 0, len(nums)

- while low < high:
  - mid = low + (high-low) // 2
  - if mid > high:
    - low = mid + 1
  else:
    - high = mid - 1
  - this will typically return the minimum, but there is a case that low is [9] in a list of [9, 0, 1, 2]
  - in cases like this, check that low and high are next to each other and if high is less than low
- return nums[low]

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1


        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 
            if low + 1 == high and nums[low] > nums[low + 1]:
                return nums[low + 1]
        return nums[low] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm uses binary search so time complexity is O(log(n))
- One weak area is that the last if statement, while does solve the test cases where low and high would be something like [9,0], it is not the most elegant. 
  - I would defintely try to see if there is way to better showcase why it is needed, or an alternate solution where it wouldn't be needed
