1. Share questions you would ask to help understand the question:
- Can the values in nums or target be negative
- Are the values in nums unique?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Binary Search (Likely)
- Two pointer (Likely)

3. Write out in plain English what you want to do: 
- The run time constraint and the array being sorted means that a viable solution is to use binary search 
- However, since the array has been rotates x times, some changes to the conditionals need to be made
- First, set up low and high 
- Then check is low is less than or equal to mid
  - If it is, then this half is sorted, and check it 
    - if target is greater than mid or less than low, then it is out of range. 
    - set low to mid + 1
  - else:
    - if it is range, set high to mid - 1
- Else (check the right half)
  - check if target is less than mid or greater than high
    - if so, then it is out of right 
    - set high to mid - 1
  else:
    - it is in range, so it low to mid + 1

- where each half is searched depending in the values of low, mid, and high

4. Translate each sub-problem into pseudocode:
- Setting up low, mid to 0, len(nums) - 1
- while low <= high:
  - mid = low + (high - low) // 2
  - if mid is equal to target, return mid 
  - if low <= mid:
    - if target > mid or target < low:
      - low = mid + 1 
    - else:
      - high = mid - 1
  - else:
    - if target < mid or target > high:
      - high = mid - 1
    - else:
      - low = mid + 1 

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else: 
                    high = mid - 1
            else: 
                if target > nums[high] or target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that since binary search is used for the algorithm, the time complexity is O(log(n))
- One weak area is that it can be hard to read
  - originally only the first if statement was used to, but since the left half could be rotated, there needed to be another check for the right half
    - This is what led to two sets of nested if statements. 