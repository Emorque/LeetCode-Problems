1. Share 2 questions you would ask to help understand the question:
- Can this be done without additional data structures?
- Can there be nums where there are only 1 or 2 colors present?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Multiple Pointers (Likely)
- Sorting (Unlikely)
  
3. Write out in plain English what you want to do: 
- Since we cannot use the library's sort function, it does not make sense to then make a sorting algorithm.
- Another way that this problem could be solved, is by using multiple pointers, called beg, mid, and end for 0, 1, and 2 respectively 
- By comparing the values at each pointer, we can deduce which values to move around and then have a sorted array

4. Translate each sub-problem into pseudocode:
- intiailize 3 pointers, beg, mid, end at 0, 0 and len(s) -1 respectively
  - while mid < end:
    - if mid is pointing to a 0, swap the values from it with beg
      - increment mid and beg by 1
    - if mid if pointing to a 1, just increment mid by 1
    - if mid if pointing to a 2, swap the values from it with end
      - decrement end by 1    

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg, mid, end = 0, 0, len(nums) -1

        while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                beg += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it does the problem without manually sorting each element
- One weak area is that the space complexity is not the best. There is a unique solution that does one pass to get all of the 0s, 1s, and 2s, and then places them back onto nums