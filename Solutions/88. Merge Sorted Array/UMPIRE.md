1. Share questions you would ask to help understand the question:
- Are the lists provided guaranteed fill the entire nums1 list?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer (Likely)

3. Write out in plain English what you want to do: 
- At first, my thought was to go from left to right for each list, and then add the smaller current number for either list to the current index on nums1. 
    - The issue with this approach is that the nums1 list would essentially have to be shifted to the right by how ever number of elements are after the current index
- However, I realized that I could use the m and n values to my advantage
- Basically, I'll go to the last number in each list and add the largest number to the end of the nums1 list and then repeat this process 

4. Translate each sub-problem into pseudocode:
- Initialize pointers at the last numbers of nums1, nums2, and last index of nums1
- While the end pointer is not at the front of the list, compare the current numbers
    - Move the current largest number at the end of the nums1 list and adjust the pointers accordingly 

5. Translate the pseudocode into Python and share your final answer:
<!--- 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        end = len(nums1) - 1

        while end >= 0:
            if p2 < 0:
                return
            if p1 < 0:
                nums1[end] = nums2[p2]
                p2 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[end] = nums1[p1]
                nums1[p1] = nums2[p2]
                p1 -= 1
            else:
                nums1[end] = nums2[p2]
                nums2[p2] = 0
                p2 -= 1
            end -= 1
        --->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm runs in O(m + n) time 
- One weak area is that while the logic makes sense, I could definetly rework the conditionals to maintain logic but have cleaner code